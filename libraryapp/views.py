from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
# Create your views here.
def books(request, filterBy=None):
    books = Book.objects.all()
    if filterBy:
        books = Book.objects.filter(genre__name__icontains=filterBy)
    return render(request, "index.html", {"books":books})

def issued_books(request):
    return render(request, "issuedbooks.html")