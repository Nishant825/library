from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


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
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("/")
    return render(request, "login.html")

def user_logout(request):
    logout(request)
    return redirect("login")