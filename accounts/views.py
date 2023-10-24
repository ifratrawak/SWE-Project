from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import UserRegisterForm, SignUpForm, ProfilePicForm
from django.contrib import messages

from .models import Profile


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

#new reg function
def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            #login user:
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registered successfully! Welcome")
            return redirect('home')
        else:
            messages.success(request, "Problem Registering. Try Again")
            return redirect('register1')

    else:
        return render(request, 'register1.html',{
            'form':form
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


def profile(request, pk):
    if request.user.is_authenticated:

        profile = Profile.objects.get(user_id=pk)
        return render(request, 'profile.html', {
            'profile': profile
        })

    else:
        messages.success(request, "You must be logged in")
        return redirect('home')

def update_profile(request):

        if request.user.is_authenticated:
            current_user = User.objects.get(id=request.user.id)
            profile_user = Profile.objects.get(user_id=request.user.id)

            user_form = SignUpForm(request.POST or None, request.FILES or None, instance=current_user)
            profile_form = ProfilePicForm(request.POST or None, request.FILES or None, instance=profile_user)

            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()

                login(request, current_user)
                messages.success(request, "Your Profile has been Updated")
                return redirect('home')
            return render(request, 'update_profile.html', {
                'user_form': user_form,
                'profile_form': profile_form
            })

        else:
            messages.success(request, "You must be logged in!")
            return redirect('home')





