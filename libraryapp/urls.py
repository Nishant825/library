from django.urls import path
from .views import *


urlpatterns = [
    path('<str:filterBy>/', books, name='home'),
    path('', books, name='home'),
    path('books', issued_books, name='books')
]