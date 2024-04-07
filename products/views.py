from venv import create
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from products.form import SearchForm
from products.models import Product, Category, SizeVariant
from products.models import Size, Quantity
from accounts.models import ProductCustomization
from accounts.models import *

def get_products(request, slug):
    try:
        product = Product.objects.get(slug =  slug)
        size_variant = SizeVariant.objects.all()
            
        return render(request, 'product/product.html', {'product': product, 'size_variant': size_variant}, )

    except Exception as e:
        print(e)


def customization(request):
    user = request.user

    if not user.is_authenticated:
        return redirect('login')
    
    if request.method == 'POST':
        product_name = request.POST['product_name']
        size = request.POST['size']
        quantity = request.POST['quantity']
        nighty_length = request.POST['nighty_length']
        sleeve_type = request.POST['sleeve_type']
        feeding_type = request.POST['feeding_type']
        zip_type = request.POST['zip_type']
        customization = ProductCustomization(user = user, product_name = product_name, size = size, quantity = quantity, nighty_length = nighty_length, sleeve_type = sleeve_type, feeding_type = feeding_type, zip_type = zip_type)
        customization.save()   
    return render(request, 'product/customization.html')

    
   

def add_to_cart(request, uid):
    
    try:
        product = Product.objects.get(uid = uid)
        user = request.user
        size = request.POST.get('size')
        quantity = request.POST.get('quantity')

        if request.method == 'POST':
            size = request.POST.get('size')
            quantity = request.POST.get('quantity')
            size = Size(size = size)
            size.save()
            quantity = Quantity(quantity = quantity)
            quantity.save()
    
        if not user.is_authenticated:
            return redirect('login') 
        
        elif product.in_stock:
            cart, _ = Cart.objects.get_or_create(user = user, is_paid = False)
            cart_item = CartItems.objects.create(cart = cart, product = product, size = size, quantity = quantity) 
            cart_item.save()
        else:
            return redirect('index')
            
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
