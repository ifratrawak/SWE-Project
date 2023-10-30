from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from stores.models import Store


def home(request):

    return render(request, 'home.html', {
        'rawak_fb': 'https://www.facebook.com/ifrattanzeef.rawak/'
    })

def nav1(request):

    return render(request, 'nav1.html',{

    })


def about(request):

    return render(request, 'about.html',{

    })