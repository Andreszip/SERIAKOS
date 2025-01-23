from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'base.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # Guarda el usuario en la base de datos
            login(request, user)  # Inicia sesión automáticamente después del registro
            messages.success(request, f'Cuenta creada con éxito. ¡Bienvenido, {user.username}!')
            return redirect('home')  # Redirige al usuario a la página principal (ajusta esta URL según tu proyecto)
    else:
        form = UserRegisterForm()

    return render(request, 'Users/register.html', {'form': form})
