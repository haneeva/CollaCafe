from django.urls import path
from .views import ViewReservation

app_name = 'reservation'

urlpatterns = [
    path('add_reservation/', ViewReservation.as_view(), name='add_reservation'),
]
