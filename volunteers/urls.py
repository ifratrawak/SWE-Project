from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns=[
    path('volunteer-reg/', views.volunteer_reg, name = 'volunteer-reg'),
    path('volunteer-profile-update/<int:v_id>', views.volunteer_update, name = 'volunteer-profile-update'),
    path('volunteer-profile/', views.volunteer_profile, name='volunteer-profile'),

    path('volunteer-request-order/<int:v_id><int:o_id>', views.volunteer_request_order, name='volunteer-request-order'),
    path('volunteer-orders/<int:s_id><int:v_id>', views.volunteer_orders, name='volunteer-orders'),

]