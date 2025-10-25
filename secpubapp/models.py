from django.db import models
from django.forms import forms

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    description = models.TextField()
    publication_year = models.PositiveBigIntegerField()

     



    
