from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    
    def __str__(self):
        return self.first_name +" "+self.last_name



class Genre(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self): 
        return self.name


STOCK_CHOICES = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )

class Book(models.Model):
    cover_img = models.ImageField(upload_to='images')
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)
    availability_status = models.CharField(max_length=3, choices=STOCK_CHOICES, default='yes')
 

    def __str__(self):
        return self.title


class BookBorrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    due_date = models.DateField(null=True)
    return_date = models.DateField(null=True, blank=True)
    fine = models.PositiveIntegerField(null=True, blank=True)
    
    def calculate_due_date(self):
        if self.return_date and self.due_date:
            if  (self.return_date - self.due_date).days > 0:
                return True
        return False

    def __str__(self):
        return self.book.title
