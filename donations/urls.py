from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views as doner_views

urlpatterns = [
    path('doner-reg', doner_views.doner_registration, name='doner-reg'),
]