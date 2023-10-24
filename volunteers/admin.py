from django.contrib import admin

from volunteers.models import Volunteer, WebUser

# Register your models here.

admin.site.register(Volunteer)
admin.site.register(WebUser)