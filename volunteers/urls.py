from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns=[
    path('webuser-reg/', views.webuser_reg, name = 'webuser-reg'),
]