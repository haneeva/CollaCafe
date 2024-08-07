from django.urls import path
from .views import ViewContact

app_name = 'contact'

urlpatterns = [
    path('', ViewContact.as_view(), name='contact'),
]
