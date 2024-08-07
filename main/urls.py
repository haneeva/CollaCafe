from django.urls import path
from .views import Index, About

app_name = 'main'

urlpatterns = [
    path('', Index.as_view(), name='main'),
    path('about', About.as_view(), name='about'),
]
