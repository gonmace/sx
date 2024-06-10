from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

def home(request):
    if request.user.is_authenticated:
        return redirect('/galeria/')
    else:
        return redirect('/login/')


class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True  # Redirige a los usuarios ya autenticados
    next_page = reverse_lazy('galeria:galeria_list')