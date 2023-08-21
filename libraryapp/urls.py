from django.urls import path
from .views import *


urlpatterns = [
    path('<str:filterBy>/', books, name='home'),
    path('', books, name='home'),
    path('books', issued_books, name='books'),
    path('users', search_user , name='search_user'),
    path('assign_book', assign_book , name='assign_book')
]