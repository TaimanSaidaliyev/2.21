from django.shortcuts import render, redirect
from .forms import *
from django.urls import reverse


def view_products(request):
    products = Product.objects.all()
    template = 'superMarket/products_list.html'
    context = {
        'products': products,
        'title': 'check'
    }
    return render(request, template, context)


def view_detail_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    template = 'superMarket/product_detail.html'
    context = {
        'product': product
    }
    return render(request, template, context)


def add_product(request):
    template = 'superMarket/product_add.html'
    form = AddProductForm(request.POST, request.FILES)
    model = Product

    if request.method == 'POST':
        if form.is_valid():
            model.object = form.save()
            model.object.save()
            return redirect('/products')
    context = {
        'form': form
    }
    return render(request, template, context)


def delete_product(request, product_id):
    product = Product.objects.filter(pk=product_id)
    product.delete()
    return redirect(reverse('view_products'))