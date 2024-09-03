from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .forms import ReservationForm
from django.contrib.auth.mixins import LoginRequiredMixin


class ViewReservation(LoginRequiredMixin, View):

    def get(self, request):
        form = ReservationForm()
        context = {'form': form}
        return render(request, 'reservationForm.html', context)

    def post(self, request):
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Reservation submitted successfully!")
            return redirect('reservation:add_reservation')
        else:
            messages.error(request, "There was an error with your submission.")
            context = {'form': form}
            return render(request, 'reservationForm.html', context)
