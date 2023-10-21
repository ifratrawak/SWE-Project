from django import forms

from stores.models import Store

# admin superuser createform
class ShopCreationForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = [
            'name',
            'location',
            'owner',
            'store_img'
        ]




class ShopUpdationForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = [
            'name',
            'location',
            'owner',
            'store_img'
        ]

#user createform
class ShopCreationFormUser(forms.ModelForm):
    class Meta:
        model = Store
        fields = [
            'name',
            'location',
            'store_img'
        ]

class ShopUpdationFormUser(forms.ModelForm):
    class Meta:
        model = Store
        fields = [
            'name',
            'location',
            'store_img'
        ]
