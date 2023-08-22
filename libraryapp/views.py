from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Book
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import BookBorrow



@login_required(login_url="login")
def books(request, filterBy=None):
    books = Book.objects.all()
    if filterBy:
        books = Book.objects.filter(genre__name__icontains=filterBy)
    return render(request, "index.html", {"books":books})

def issued_books(request):
    return render(request, "issuedbooks.html")


def search_user(request):
    user = request.GET.get("user_name", None)
    if user:
        user_obj = list(User.objects.filter(first_name__icontains=user).values("first_name"))
        return JsonResponse({"users":user_obj, "status":True})
    return JsonResponse({"users":user_obj, "status":False})

def assign_book(request,book_id):
    user_list = list(User.objects.all().values_list("username", flat=True))
    book_obj = Book.objects.get(id=book_id)
    return render(request, "bookassign.html", {"books":book_obj, "user_list_obj":user_list})


def borrow_book(request):
    books_list = BookBorrow.objects.all()
    print(books_list,"909009")
    return render(request, "issuedbooks.html", {"books":books_list})