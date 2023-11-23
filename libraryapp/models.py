from django.db import models
from django.contrib.auth.models import User
from django.core.cache import cache

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
 
    def save(self, *args, **kwargs):
        cache.delete('books')
        super(Book, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title


class BookBorrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    due_date = models.DateField(null=True)
    
    class Meta:
       ordering = ['-id']
    
    def format_name(self):
        return f"{self.user.first_name.capitalize()} {self.user.last_name.capitalize()}"

    def __str__(self):
        return self.book.title


class BookBorrowHistory(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    due_date = models.DateField(null=True)
    fine = models.PositiveIntegerField(default=0)
    return_date = models.DateField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    class Meta:
       ordering = ['-id']
    
    def format_name(self):
        return f"{self.user.first_name.capitalize()} {self.user.last_name.capitalize()}"

    def calculate_fine(self):
        charges = (self.due_date - self.return_date).days
        if self.due_date:
            if charges<0:
                charges = abs(charges)*20
            else:
                charges = 0
            return charges

    def __str__(self):
        return self.book.title