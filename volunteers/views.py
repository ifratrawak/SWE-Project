from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from volunteers.forms import VolunteerRegForm
from . import forms


# Create your views here.

def volunteer_reg(request):
    if request.method == 'POST':
        user =User.objects.get(user=request.user)
        vol_form = forms.VolunteerRegForm(request.POST, request.FILES)
        if vol_form.is_valid():
            volunteer=vol_form.save(commit=False)
            volunteer.user=request.user
            volunteer.save()


            return redirect('/')

    else:
        vol_form = forms.VolunteerRegForm(request.POST, request.FILES)

    return render(request, 'volunteer_reg.html',{
        'vol_form':vol_form
    })

