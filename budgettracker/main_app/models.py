from django.db import models

# Create your models here.
class Category(models.Model):
    income =models.IntegerField()
    expense = models.IntegerField()
    
    def __str__(self):
        return self.name
    