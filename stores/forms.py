from django import forms

from stores.models import Store, Product, Order


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

class ProductCreationFormUser(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'category',
            'quantity',
            'description',
            'image'
        ]

class ProductCreationFormAdmin(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'store',
            'name',
            'category',
            'quantity',
            'description',
            'image'
        ]
class ProductUpdationFormUser(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'category',
            'quantity',
            'description',
            'image'
        ]
class OrderCreationFormUser(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'product',
            'quantity',
            'date',
            # 'status'
        ]