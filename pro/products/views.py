from django.shortcuts import render, redirect
from .forms import ProductForm

def upload_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect to a product list view (to be created)
    else:
        form = ProductForm()
    return render(request, 'products/upload_product.html', {'form': form})

    # products/views.py
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})