from django.contrib import admin
from .models import ExtendedUser, Donation
# Register your models here.
admin.site.register(ExtendedUser)
admin.site.register(Donation)