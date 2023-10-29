from django.contrib import admin

from volunteers.models import Volunteer, VolunteerRequest

# Register your models here.

admin.site.register(Volunteer)
admin.site.register(VolunteerRequest)
