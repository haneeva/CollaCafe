from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['customer_name', 'customer_email',
                  'customer_phone', 'reservation_date', 'reservation_time', 'number_of_guests']
