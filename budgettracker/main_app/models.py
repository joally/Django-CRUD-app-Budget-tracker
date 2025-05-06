from django.db import models


class Record(models.Model):

    creation_date = models.DateTimeField(auto_now_add=True)

    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    email = models.CharField(max_length=255)

    phone = models.CharField(max_length=20)

    address = models.CharField(max_length=300)

    city = models.CharField(max_length=255)

    province = models.CharField(max_length=200)

    country = models.CharField(max_length=125)


    def __str__(self):

        return self.first_name + "   " + self.last_name



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
    
