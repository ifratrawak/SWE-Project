from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views as user_views

urlpatterns = [
    path('register/', user_views.register, name='register'),
    path('login/', user_views.login_view, name='login'),
    path('logout/', user_views.logout_view, name='logout'),
    path('register1/', user_views.register_user, name='register1'),
    path('profile/<int:pk>', user_views.profile, name='profile'),
    path('update-profile/', user_views.update_profile, name='update-profile'),
]
