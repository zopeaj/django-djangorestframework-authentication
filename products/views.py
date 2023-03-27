from django.shortcuts import render, redirect
from django.views import View
from products.models import Product
from products.forms import ProductUpdateForm, ProductCreateForm
from django.conf.urls import reverse
from django.contrib import message
# Create your views here.

def add_product_view(request):
    product = Product.objects.all()
    if request.method == 'POST':
        form = ProductCreateForm(request.POST)
        if form.is_valid():
            form.save()
            message.success('Product created successfully')
            return redirect(reverse('product:home'))

    ctx = { 'form': form, 'product': product }

    return render(request, 'products/home.html', ctx)

def get_product_view(request, pk):
    if request.method == 'GET':
        product = Producut.objects.get(id=pk)
        if product is not None:
            ctx = {'product': product }
            return render(request, 'products/detail.html', ctx)

def update_product_view(request, pk):
    if request.method == 'PUT':
        product = Product.objects.get(id=pk)
        form = ProductUpdateForm(request.POST)
        if form.is_valid():
            form.save()
    ctx = { 'form': form }
    return render(request, 'products/update.html', ctx)

def delete_product_view(request, pk):
    product = Product.objects.get(id=pk)
    if product is not None:
        product.delete()
        return redirect(reverse('product:home'))
    return render(request, 'products/delete.html')
