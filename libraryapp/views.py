from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Book, BookBorrowHistory
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import BookBorrow
from accounts.permissions import staff_permission_required
from datetime import datetime

@login_required(login_url="login")
def books(request, filterBy=None):
    books = Book.objects.all()
    if filterBy:
        books = Book.objects.filter(genre__name__icontains=filterBy)
    return render(request, "index.html", {"books":books})

@staff_permission_required
def issued_books(request):
    return render(request, "issuedbooks.html")


def search_user(request):
    user = request.GET.get("user_name", None)
    if user:
        user_obj = list(User.objects.filter(first_name__icontains=user).values("first_name"))
        return JsonResponse({"users":user_obj, "status":True})
    return JsonResponse({"users":user_obj, "status":False})

@staff_permission_required
def assign_book(request,book_id):
    user_list = list(User.objects.all().values_list("username", flat=True))
    book_obj = Book.objects.get(id=book_id)
    if request.method == "POST":
        title_data = request.POST.get("title_data")
        username  = request.POST.get("username")
        due_date = request.POST.get("due_date")
        user = User.objects.get(username=username)
        book = Book.objects.get(title=title_data)
        book_obj = BookBorrow.objects.create(user=user, due_date=due_date, book=book)
        book_obj.book.availability_status = "no"
        book_obj.book.save()
        if book_obj:
            return redirect("issued_books")
    return render(request, "bookassign.html", {"books":book_obj, "user_list_obj":user_list})

@staff_permission_required
def borrow_book(request):
    books_list = BookBorrow.objects.all()
    return render(request, "issuedbooks.html", {"books":books_list})

def return_books(request):
    issed_book_id = request.POST.get("issed_book_id", None)
    issued_book_obj = BookBorrow.objects.get(id=issed_book_id)
    book_value = request.POST.get("book_value", None)
    book_value = Book.objects.get(id=book_value)
    user = request.POST.get("user", None)
    user = User.objects.get(id=user)
    due_date = request.POST.get("due_date", None)
    date_object = datetime.strptime(due_date, "%d-%m-%Y")
    if issued_book_obj and book_value and due_date and user:
        issued_book_obj.delete()
        borow_book = BookBorrowHistory.objects.create(book = book_value, due_date=date_object, user=user)
        if borow_book:
            return JsonResponse({"status":True})
        else:
            return JsonResponse({"status":False})
        


@staff_permission_required
def issued_borrow_history(request):
    books_list = BookBorrowHistory.objects.all()
    return render(request, "issued_history.html", {"books":books_list})


def fine_paid(request):
    if request.method == "POST":
        book_id = request.POST.get("book_id")
        paid = request.POST.get("paid")
        fine_val = request.POST.get("fine_val")
        print(fine_val,"$$$$$$$$$$$$$")
        book_obj = BookBorrowHistory.objects.get(id=book_id)
        if not fine_val:
            fine_val = 0
        if book_obj:
            book_obj.paid = bool(int(paid))
            book_obj.fine = fine_val
            book_obj.save()
            return JsonResponse({"status":True})
        else:
            return JsonResponse({"status":False})
