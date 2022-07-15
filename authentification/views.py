from django.conf import settings
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render

from . import forms


def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentification/signup.html', context={'form': form})

def login_page(request):

    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                message = "Identifiants invalides.Ou vous n'êtes pas encore inscrire au système de santé"

    return render(request, 'authentification/login.html',
                  context={'form': form, 'message': message})


def logout_user(request):
    logout(request)
    return redirect('login')