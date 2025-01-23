# accounts/urls.py

from django.urls import path
from .views import register, home

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', register, name='register'),  # Ruta para el registro
]
