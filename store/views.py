from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def home(request):
    return render(request, 'index.html')

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()
    return render(request, 'shop.html', {'category': category, 'products': products})

def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    return render(request, 'shop_detail.html', {'product': product})

def contact(request):
    return render(request, 'contact.html')

