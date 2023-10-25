from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from volunteers.forms import VolunteerRegForm
from . import forms


# Create your views here.

def volunteer_reg(request):
    if request.method == 'POST':
        if request.user.is_superuser:
            vol_form = forms.VolunteerRegForm(request.POST, request.FILES)
            if vol_form.is_valid():
                vol_form.save()

                return redirect('home')

        else:
            vol_form = forms.VolunteerRegFormUser(request.POST, request.FILES)

            if vol_form.is_valid():
                vol = vol_form.save(commit=False)
                vol.volunteer = request.user
                vol.save()

                return redirect('/')

    else:
        #just going to page, not submitting
        if request.user.is_superuser:
            vol_form = forms.VolunteerRegForm(request.POST, request.FILES)
        else:
            vol_form = forms.VolunteerRegFormUser(request.POST, request.FILES)

    return render(request, 'volunteer_reg.html',{
        'vol_form':vol_form
    })

