from django.http import HttpResponse
from django.shortcuts import render
from . import forms

# Create your views here.
def food_donation(request):
    if request.method == 'POST':
        don_form = forms.FoodDonationForm(request.POST or None)
        print('form is created')
        if don_form.is_valid():
            don_form.save()
            return HttpResponse('food donate successfully')
    else:
        don_form = forms.FoodDonationForm(request.POST or None)
    return render(request, 'food_donateform.html', {
        "don_form": don_form
    })


def become_doner(request):

    return render(request, 'become_doner.html', {

    })





#def food_donation(request):
   # return render(request, 'base.html',{

   # })

