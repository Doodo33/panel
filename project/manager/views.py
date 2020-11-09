from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('searching_report')
            else:
                messages.info(request, "Username OR password is incorrect")
        return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def homepage(request):
    return render(request, 'home.html')


def password_change(request):
    return render(request, 'password_change.html')


@login_required(login_url='login')
def searching_client(request):
    return render(request, 'services/searching_client.html')


@login_required(login_url='login')
def searching_report(request):
    return render(request, 'services/searching_report.html')


@login_required(login_url='login')
def adding_report(request):
    return render(request, 'services/adding_report.html')

