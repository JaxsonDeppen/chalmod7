from django.db import models

# Create your models here.
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)

    


class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_date = models.DateField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    
  

class Loan(models.Model):
    book = models.ForeignKey(Book, related_name='loans', on_delete=models.CASCADE)
    borrower = models.CharField(max_length=255)
    loan_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)

   
