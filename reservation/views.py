from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .forms import ReservationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Reservation
from django.utils.dateparse import parse_date


class ViewReservationAdd(LoginRequiredMixin, View):

    def get(self, request):
        form = ReservationForm()
        context = {'form': form}
        return render(request, 'reservationForm.html', context)

    def post(self, request):
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            messages.success(request, "Reservation submitted successfully!")
            return redirect('reservation:add_reservation')
        else:
            messages.error(request, "There was an error with your submission.")
            context = {'form': form}
            return render(request, 'reservationForm.html', context)


class ViewReservationList(LoginRequiredMixin, View):
    def get(self, request):
        reservations = Reservation.objects.filter(user=request.user)

        # Get the date from the query parameters
        filter_date = request.GET.get('date')

        if filter_date:
            try:
                filter_date = parse_date(filter_date)
                reservations = reservations.filter(
                    reservation_date=filter_date)
            except ValueError:
                # Handle invalid date input if needed
                pass

        context = {'reservations': reservations}
        return render(request, 'reservationList.html', context)
