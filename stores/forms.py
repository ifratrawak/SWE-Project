from django import forms

from stores.models import Store


class ShopCreationForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = [
           'name',
            'location',
            'owner',

        ]

class ShopUpdationForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = [
             'name',
            'location',
            'owner',
                ]
