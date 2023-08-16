from django.shortcuts import render

def user_signup(request):
    return render(request, "signup.html")

def user_login(request):
    return render(request, "login.html")
