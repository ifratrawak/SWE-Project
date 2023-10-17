from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('store', views.create_shop, name='create-store'),
    path('create-shop/', views.create_shop, name='create-shop'),
    path('update-shop/<int:s_id>', views.update_shop, name='update-shop'),
    path('delete-shop/<int:s_id>', views.delete_shop, name='delete-shop'),
    path('view-shops/', views.view_shops, name='view-shop'),


]
