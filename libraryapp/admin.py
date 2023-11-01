from django.contrib import admin
from .models import Author, Book, Genre, BookBorrow, BookBorrowHistory


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(BookBorrow)
admin.site.register(BookBorrowHistory)

