from django.urls import path
from .views import *


urlpatterns = [
    path('<str:filterBy>/', books, name='home'),
    path('', books, name='home'),
    path('users', search_user , name='search_user'),
    path('assign_book/<book_id>', assign_book , name='assign_book'),
    path('issued_books', borrow_book , name='issued_books'),
    path('return_books', return_books , name='return_books'),
    path('issued_history', issued_borrow_history , name='issued_borrow_history'),
    path('fine_paid', fine_paid , name='fine_paid')

]