from django.urls import path
from .views import *


urlpatterns = [
    path('<str:filterBy>/', books, name='home'),
    path('', books, name='home'),
    path('users', search_user , name='search_user'),
    path('assign_book/<book_id>', assign_book , name='assign_book'),
    path('issued_books', borrow_book , name='issued_books')
]