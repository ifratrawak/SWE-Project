from django import forms

from volunteers.models import WebUser, Volunteer


class VolunteerRegForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = [

        ]


class WebUserForm(forms.ModelForm):
    class Meta:
        model = WebUser
        fields = [
            'name',
            'phone',
            'location',
            'address',
            'gender',
            'photo',
        ]
