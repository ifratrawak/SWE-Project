from django import forms

from volunteers.models import Volunteer


class VolunteerRegForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = [
            'volunteer',
            'is_available',
            'store',
        ]


class VolunteerRegFormUser(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = [
            'is_available',
            'store'
        ]


class VolunteerUpdFormUser(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = [
            'is_available',
            'store'
        ]
