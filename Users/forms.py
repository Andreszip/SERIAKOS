# accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Requerido. Introduce un correo válido.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # Campos que quieres usar en el formulario
