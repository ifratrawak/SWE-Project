from django.shortcuts import render
from stores.models import Store
from django.http import HttpResponse
from .import forms



# Create your views here.

# def create_store(request):
#     stores = Store.objects.all()
#     return render(request, 'home.html', {
#         "stores": stores
#     })



def create_shop(request):
    if request.method== 'GET':
        form = forms.ShopCreationForm(request.GET)

        if form.is_valid():
            form.save()

            return HttpResponse("Shop Created Successfully")

    else:
        form = forms.ShopCreationForm()

    return render(request, 'form.html', {
        'form':form
    })
def update_shop(request, s_id):
    store = Store.objects.get(pk =s_id)
    if request.method == 'GET':
        form = forms.ShopUpdationForm(request.GET, instance=store)
        print("Shop Updated")
        if form.is_valid():
            form.save()
            return HttpResponse("Shop Updated Successfully!")

    else :
        form = forms.ShopUpdationForm(instance=store)

    return render(request, 'form.html', {
        'form':form
    })

def view_shops(request):
    stores = Store.objects.all()
    return render(request, 'store.html',{
        'stores':stores
    })

from django.shortcuts import render, redirect


def delete_shop(request, s_id):
    Store.objects.get(pk=s_id).delete()

    return redirect('/')
