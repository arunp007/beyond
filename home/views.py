from django.shortcuts import render
from products.models import Product, Category


def index(request):
    products = Product.objects.all()
    category = Category.objects.all() 
    return render(request, 'home/index.html', {'products': products, 'category': category})
