from django.urls import path
from .views import *


urlpatterns = [
    path('', books, name='home'),
    path('books', issued_books, name='books')
]