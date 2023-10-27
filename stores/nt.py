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