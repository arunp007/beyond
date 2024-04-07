from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

def login_page(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user_obj = User.objects.filter(username = email)

        if not user_obj.exists():
            messages.warning(request, "Your account not found.")
            return HttpResponseRedirect(request.path_info)
        
        user_obj = authenticate(username = email, password = password)
        
        if user_obj:
            login(request, user_obj)
            return redirect('/')
        
        messages.warning(request, "Invalid credentials.")
        return HttpResponseRedirect(request.path_info)

    return render(request, 'accounts/login.html')

def signup_page(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']

        user_obj = User.objects.filter(username = email)

        if user_obj.exists():
            messages.warning(request, "Email is already exist.")
            return HttpResponseRedirect(request.path_info)
        
        user_obj = User.objects.create(first_name = first_name, last_name = last_name, email = email, username = email)
        user_obj.set_password(password)
        user_obj.save()

        messages.success(request, "Successfully registered. Login now")
        return HttpResponseRedirect(request.path_info)

    return render(request, 'accounts/signup.html')





