from django.contrib import admin
from django.contrib.auth.models import User, Group
from accounts.models import Profile


# Register your models here.

class ProfileInline(admin.StackedInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    model = User
    fields = [
        'username',
        # 'email_address',
        # 'staff_status',
    ]
    inlines = [ProfileInline]


#admin.site.unregister(User)
#admin.site.register(User, UserAdmin)

admin.site.register(Profile)
# # mix profile info with user info
