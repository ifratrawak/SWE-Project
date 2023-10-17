from django.shortcuts import render

from stores.models import Store


def home(request):

    return render(request, 'home.html', {

    })

