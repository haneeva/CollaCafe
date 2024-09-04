from django.contrib import admin
from .models import Reservation

# Register your models here.


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_email',
                    'customer_phone', 'reservation_date', 'reservation_time', 'number_of_guests', 'user')


admin.site.register(Reservation, ReservationAdmin)
