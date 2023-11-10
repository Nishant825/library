from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.conf import settings
import requests
import json
from django.contrib import messages
from .tasks import send_email

def user_signup(request):

    if request.method == "POST":
        first_name = request.POST.get("username")
        last_name = request.POST.get("password")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        if first_name and last_name and username and email and password:
            send_email.delay(username, email)
            
            user = User.objects.create_user(first_name=first_name, last_name=last_name,
                                            username=username, email=email, password=password, is_active=False)
            if user:
                return render(request, "login.html", {"from_signup":True})
        else:
            pass
    return render(request, "signup.html")

def user_login(request):
    error_occurred = False
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
        if result['success']:
            user = authenticate(username=username, password=password)
            if user and user.is_active:
                login(request, user)
                return redirect("/")
            error_occurred = True
            messages.error(request, 'given credentials is incorrect or account is not activated')
        else:
            messages.error(request, 'Invalid reCAPTCHA. Please try again.')
    return render(request, "login.html", {"error_occurred":json.dumps(error_occurred)})

def user_logout(request):
    logout(request)
    return redirect("login")


def activate_account(request, username):
    user = User.objects.get(username=username)
    if user:
        user.is_active = True
        return render(request, 'signup_success.html')