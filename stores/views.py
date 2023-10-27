from django.shortcuts import render
from stores.models import Store, Product, Order
from django.http import HttpResponse
from . import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

from .forms import ShopUpdationForm, ShopCreationFormUser, ShopUpdationFormUser, OrderCreationFormUser


# Create your views here.

# def create_store(request):
#     stores = Store.objects.all()
#     return render(request, 'home.html', {
#         "stores": stores
#     })


def create_store(request):

    if request.method == 'POST':

        if request.user.is_superuser:
            form = forms.ShopCreationForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()

                return redirect('/stores/view-shops/')
        else:
            form = forms.ShopCreationFormUser(request.POST, request.FILES)

            if form.is_valid():
                store = form.save(commit=False)
                store.owner = request.user  # logged in user made manager
                store.save()

                return redirect('/stores/view-shops/')

    else:
        # just going to page, not submitting
        if request.user.is_superuser:
            form = forms.ShopCreationForm(request.POST, request.FILES)
        else:
            form = forms.ShopCreationFormUser(request.POST, request.FILES)

    return render(request, 'create_store.html', {
        'form': form,

    })


# not using update_store() function
# instead we are using upd_store() function. Scroll down to see it
def update_store(request, s_id):
    store = Store.objects.get(pk=s_id)
    if request.method == 'GET':
        form = forms.ShopUpdationForm(request.GET, instance=store)
        print("Shop Updated")
        if form.is_valid():
            form.save()
            return HttpResponse("Shop Updated Successfully!")

    else:
        form = forms.ShopUpdationForm(instance=store)

    return render(request, 'update_store.html', {
        'form': form
    })


def view_shops(request):
    stores = Store.objects.all()
    return render(request, 'store.html', {
        'stores': stores
    })


from django.shortcuts import render, redirect


def delete_shop(request, s_id):
    Store.objects.get(pk=s_id).delete()

    return redirect('/')


def store_profile(request, s_id):
    store = Store.objects.get(pk=s_id)
    return render(request, 'store_profile.html', {
        'store': store
    })


# using this upd_store() function to update store info
def upd_store(request, s_id):
    store = Store.objects.get(pk=s_id)
    if request.user.is_superuser:

        form = ShopUpdationForm(request.POST or None, instance=store)
    else:
        form = ShopUpdationFormUser(request.POST or None, instance=store)

    if form.is_valid():
        form.save()
        return redirect("view-shop")

    return render(request, 'update_store.html', {
        'store': store,
        'form': form
    })


def all_stores(request):
    stores_list = Store.objects.all()
    return render(request, 'store_list.html', {
        'stores_list': stores_list
    })


def search_stores(request):
    if request.method == "POST":
        searched = request.POST['searched']
        stores = Store.objects.filter(name__contains=searched)

        return render(request, 'search_stores.html', {
            'searched': searched,
            'stores': stores,
        })
    else:

        return render(request, 'search_stores.html', {

        })


# view all products of all the stores
def all_products(request):
    products = Product.objects.all()
    return render(request, 'all_products.html', {
        'products': products
    })


def my_products(request):
    store = Store.objects.all()
    product = Product.objects.all()
    return render(request, 'my_products.html', {
        'product': product,
        'store': store
    })


def my_store(request):
    store = Store.objects.all()
    return render(request, 'my_store.html', {
        'store': store
    })


def add_product(request, s_id):
    store = Store.objects.get(pk=s_id)
    if request.method == 'POST':

        # if request.user.is_superuser:
        #     prod_form = forms.ShopCreationForm(request.POST, request.FILES)
        #     if prod_form.is_valid():
        #         prod_form.save()
        #
        #         return redirect('/stores/view-shops/')
        # else:
        prod_form = forms.ProductCreationFormUser(request.POST, request.FILES)

        if prod_form.is_valid():
            product = prod_form.save(commit=False)
            product.store = store  # product created under current store
            product.save()

            return redirect('/stores/my-products/')

    else:
        # just going to page, not submitting
        # if request.user.is_superuser:
        #     prod_form = forms.ShopCreationForm(request.POST, request.FILES)
        # else:
        prod_form = forms.ProductCreationFormUser(request.POST, request.FILES)

    return render(request, 'add_product.html', {
        'prod_form': prod_form,
        'store': store
    })


def upd_product(request, s_id, p_id):
    store = Store.objects.get(pk=s_id)
    product = Product.objects.get(pk=p_id)

    prod_form = forms.ProductUpdationFormUser(request.POST or None, request.FILES or None, instance=product)

    if prod_form.is_valid():
        prod_form.save()
        return redirect('/stores/my-products/')

    return render(request, 'upd_product.html', {
        'prod_form': prod_form,
        'store': store,
        'product': product
    })

def delete_product(request, s_id, p_id):
    store = Store.objects.get(pk=s_id)
    product = Product.objects.get(pk=p_id)
    product.delete()
    return redirect('/stores/my-products')

def my_store_orders(request, s_id, p_id):
    orders = Order.objects.all()

    products = Product.objects.get(pk=s_id)
    return render(request, 'my_store_orders.html',{
        'orders':orders,
        'products':products,

    })


def create_order(request, s_id):
    store = Store.objects.get(pk=s_id)
    products = Product.objects.filter(store=store)
    # problem: in forms, products of all stores are coming, instead need only that store's products
    if request.method == 'POST':
        order_form = forms.OrderCreationFormUser(request.POST or None, request.FILES or None)

        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.store = store
            order.save()
            return redirect('/stores/my-store/')

    else:
        order_form = forms.OrderCreationFormUser(request.POST or None, request.FILES or None)

    return render(request, 'create_order.html', {
        'order_form':order_form,
        'store':store,
        'products':products,

    })

