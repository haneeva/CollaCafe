from django.urls import path
from .views import ViewSignup, ViewLogin, ViewLogout

app_name = 'account'

urlpatterns = [
    path('login/', ViewLogin.as_view(), name='login'),
    path('signup/', ViewSignup.as_view(), name='signup'),
    path('logout/', ViewLogout.as_view(), name='logout'),
]
