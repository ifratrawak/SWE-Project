from django import forms

from volunteers.models import Volunteer


class VolunteerRegForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = [
            'user',
            'is_available',
            'store',

        ]


