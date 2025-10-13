from django.db import models
from django.forms import forms

# Create your models here.
class Book(models.Model):
      Book_name = models.CharField(max_length=100)
      Author_name = models.CharField(max_length=100)
      Description = models.TextField()
      Publication_year = models.PositiveBigIntegerField()

      def __str__(self):
        return self.Book_name
    
