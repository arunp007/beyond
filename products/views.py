from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from products.form import SearchForm
from products.models import Product, Category, SizeVariant
from accounts.models import *

def get_products(request, slug):
    try:
        product = Product.objects.get(slug =  slug)
        size_variant = SizeVariant.objects.all()
        return render(request, 'product/product.html', {'product': product, 'size_variant': size_variant})

    except Exception as e:
        print(e)
        

def add_to_cart(request, uid):
    variant = request.GET.get('variant')
    
    try:
        product = Product.objects.get(uid = uid)
        user = request.user
        
        if not user.is_authenticated:
            return redirect('login') 
        
        cart, _ = Cart.objects.get_or_create(user=user, is_paid=False)
        cart_item = CartItems.objects.create(cart=cart, product=product) 
        
        if variant:
            size_variant = SizeVariant.objects.get(size_name=variant)
            cart_item.size_variant = size_variant
            cart_item.save()
        
        return redirect(request.META.get('HTTP_REFERER'))
    
    except Profile.DoesNotExist:
        return redirect('signup') 


def cart(request):
    try:
        user = request.user
        if not user.is_authenticated:
            return redirect('login')
    
        cart = Cart.objects.get(is_paid=False, user=request.user)
        cart_items = CartItems.objects.filter(cart=cart)
        total_price = sum(float(cart.product.price.replace(',','')) for cart in cart_items)
        return render(request, 'accounts/cart.html', {'cart_items': cart_items, 'total_price': total_price})
    
    except Exception as e:
        print(e)
    

def remove_cart(request, cart_item_uid):
    try:
        cart_item = CartItems.objects.get(uid = cart_item_uid)
        cart_item.delete()

    except Exception as e:
        print(e)
    
    return redirect(request.META.get('HTTP_REFERER')) 


def search(request):
    form = SearchForm(request.GET)
    results = None

    if form.is_valid():
        query = form.cleaned_data['query']
        results =  Product.objects.filter(product_name__icontains=query) | Product.objects.filter(price__icontains=query) | Product.objects.filter(dummy_price__icontains=query)
    return render(request, 'product/search.html', {'form': form, 'results': results})


def maternity(request):
    category_name = 'Maternity Nighties'
    category = Category.objects.get(category_name = category_name)
    products = Product.objects.filter(category = category)
    return render(request, 'product/maternity.html', {'category_name': category_name , 'products': products})

def kaftan(request):
    category_name = 'Kaftan Nighties'
    category = Category.objects.get(category_name = category_name)
    products = Product.objects.filter(category = category)
    return render(request, 'product/kaftan.html' , {'category_name': category_name, 'products': products})

def threebyfourth_sleeve(request):
    category_name = 'Three By Fourth Sleeve Nighties'
    category = Category.objects.get(category_name = category_name)
    products = Product.objects.filter(category = category)
    return render(request, 'product/threebyfourth_sleeve.html', {'category_name': category_name, 'products': products})
