from django.shortcuts import render, redirect
from volunteers.forms import VolunteerRegForm, WebUserForm
from . import forms
from .models import WebUser


# Create your views here.

def volunteer_reg(request):
    if request.method == 'POST':
        user = WebUser.objects.get(user=request.user)
        form = forms.VolunteerRegForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('/')

    else:
        form = forms.VolunteerRegForm()

    return render(request, 'form.html',{
        'form':form
    })

def webuser_reg(request):
    if request.method == 'POST':
        user = WebUser.objects.get(user=request.user)
        form = forms.WebUserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('/')

    else:
        form = forms.WebUserForm()

    return render(request, 'volunteer_reg.html',{
        'form':form
    })
