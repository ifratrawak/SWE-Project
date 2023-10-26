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
