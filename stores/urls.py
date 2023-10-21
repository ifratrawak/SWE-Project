from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    # path('store', views.create_shop, name='create-store'),
    path('create-store/', views.create_store, name='create-store'),
    path('update-store/<int:s_id>', views.update_store, name='update-store'),
    path('delete-shop/<int:s_id>', views.delete_shop, name='delete-shop'),
    path('view-shops/', views.view_shops, name='view-shop'),

    path('store-profile/<int:s_id>', views.store_profile, name='store-profile'),
    path('upd-store/<int:s_id>', views.upd_store, name = 'upd-store'),
    path('all-stores/', views.all_stores, name="all-stores"),

    path('search-stores/', views.search_stores, name='search-stores'),



]
