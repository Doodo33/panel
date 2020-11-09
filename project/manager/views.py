from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm


def register_page(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Utworzono konto dla:' + user)

            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)


def login_page(request):
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


def homepage(request):
    return render(request, 'home.html')


def password_change(request):
    return render(request, 'password_change.html')


def searching_client(request):
    return render(request, 'services/searching_client.html')


def searching_report(request):
    return render(request, 'services/searching_report.html')


def adding_report(request):
    return render(request, 'services/adding_report.html')

