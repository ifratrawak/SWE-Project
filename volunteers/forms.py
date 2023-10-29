from django import forms

from volunteers.models import Volunteer, VolunteerRequest


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

class VolunteerRequestFormUser(forms.ModelForm):
    class Meta:
        model = VolunteerRequest
        fields = [
            'order'
        ]