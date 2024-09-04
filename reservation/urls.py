from django.urls import path
from .views import ViewReservationAdd, ViewReservationList

app_name = 'reservation'

urlpatterns = [
    path('add_reservation/', ViewReservationAdd.as_view(), name='add_reservation'),
    path('', ViewReservationList.as_view(), name='reservation'),
]
