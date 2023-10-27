from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from stores.models import Order, Product
from volunteers.forms import VolunteerRegForm
from . import forms
from .models import Volunteer


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
        # just going to page, not submitting
        if request.user.is_superuser:
            vol_form = forms.VolunteerRegForm(request.POST, request.FILES)
        else:
            vol_form = forms.VolunteerRegFormUser(request.POST, request.FILES)

    return render(request, 'volunteer_reg.html', {
        'vol_form': vol_form
    })


def volunteer_update(request, v_id):
    volunteer = Volunteer.objects.get(pk=v_id)
    vol_form = forms.VolunteerUpdFormUser(request.POST or None, request.FILES or None, instance=volunteer)

    if vol_form.is_valid():
        vol_form.save()
        return redirect('/volunteers/volunteer-profile/')

    return render(request, 'volunteer_prof_update.html', {
        'volunteer': volunteer,
        'vol_form':vol_form
    })


def volunteer_profile(request):
    volunteer = Volunteer.objects.all()
    return render(request, 'volunteer_profile.html', {
        'volunteer': volunteer
    })

def volunteer_orders(request, s_id, v_id):
    orders = Order.objects.all()
    # products = Product.objects.get(pk=s_id)
    volunteer = Volunteer.objects.get(pk=v_id)

    return render(request, 'volunteer_orders.html',{
        'orders': orders,
        'volunteer':volunteer
    })