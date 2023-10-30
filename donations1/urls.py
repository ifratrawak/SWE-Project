from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns =[
    path('food-donation/', views.food_donation, name='food-donation'),
    path('become-doner/', views.become_doner, name='become-doner'),
]