from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.contrib import messages


# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, ("Registration Successful!"))
            return redirect("/")

    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {
        'form': form
    })


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # if the user logs in for a purpose the user should automatically be redirected to that page
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {
        "form": form
    })


def logout_view(request):
    if request.method == "POST" or "GET":
        logout(request)
        messages.success(request, ("You were logged out!"))
        return render(request, 'logout.html')


def profile(request):
    pass
