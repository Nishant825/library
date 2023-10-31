from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.conf import settings
import requests
import json
from django.contrib import messages


def user_signup(request):
    if request.method == "POST":
        first_name = request.POST.get("username")
        last_name = request.POST.get("password")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        if first_name and last_name and username and email and password:
            user = User.objects.create_user(first_name=first_name, last_name=last_name,
                                            username=username, email=email, password=password)
            if user:
                return redirect("login")
    return render(request, "signup.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        recaptcha_response = request.POST.get('g-recaptcha-response')
        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=values)
        result = response.json()
        print(result,"7787878")
        if result['success']:
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect("/")
            messages.error(request, 'username or password is incorrect')
        else:
            messages.error(request, 'Invalid reCAPTCHA. Please try again.')
    return render(request, "login.html")

def user_logout(request):
    logout(request)
    return redirect("login")