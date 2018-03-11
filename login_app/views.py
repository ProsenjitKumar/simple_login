from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return render(request, 'login_app/wlc.html')
        else:
            return HttpResponse('Password or useername incorrect')
    return render(request, 'login_app/login.html')


def user_logout(request):
    logout(request)
    return HttpResponse('/login/')


def signup(request):
    form = UserCreationForm()
    return render(request, 'login_app/signup.html', {'signup_form': form})
