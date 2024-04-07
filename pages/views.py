from django.shortcuts import render
from pages.models import Contact_us

def contact_us(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        message = request.POST['message']
        contact_details = Contact_us(name = name, email = email, phone = phone_number, message = message)
        contact_details.save()
    return render(request, 'pages/contact_us.html')

def about_us(request):
    return render(request, 'pages/about_us.html')

def terms_and_condition(request):
    return render(request, 'pages/terms_and_conditions.html')

def return_and_refund(request):
    return render(request, 'pages/return_and_refund.html')

def shipping_policy(request):
    return render(request, 'pages/shipping_policy.html')

def privacy_policy(request):
    return render(request, 'pages/privacy_policy.html')
