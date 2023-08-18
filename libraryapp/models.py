from django.db import models



class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    
    def __str__(self):
        return self.first_name +" "+self.last_name



class Genre(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self): 
        return self.name


class Book(models.Model):
    cover_img = models.ImageField(upload_to='images')
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.title
