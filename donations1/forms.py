from django import forms
from .models import Donation1


class FoodDonationForm(forms.ModelForm):


    class Meta:
        model = Donation1
        fields = [
            'food_name',
            'category',
            'donation_date'
        ]

