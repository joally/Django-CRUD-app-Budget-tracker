from django.db import models
from django import forms


# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=100)
    income =models.IntegerField()
    expense = models.IntegerField()
    
    def __str__(self):
        return self.name
    

class Expense(models.Model):
    name = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='expenses')  # Assuming you have a Category model
    date = models.DateField()

    def __str__(self):
        return self.name
    
