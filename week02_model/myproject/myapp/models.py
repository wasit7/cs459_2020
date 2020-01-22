from django.db import models

# Create your models here.
class Bike(models.Model):
    start=models.DateField(auto_now=False, auto_now_add=True)
    type=models.CharField(max_length=10)
    price=models.DecimalField( max_digits=5, decimal_places=2)

class Customer(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField(auto_now=False, auto_now_add=False)
    mobile=models.CharField(max_length=20)

class Rent(models.Model):
    start=models.DateTimeField(auto_now=False, auto_now_add=False)
    stop=models.DateTimeField(auto_now=False, auto_now_add=False)
    cost=models.DecimalField( max_digits=5, decimal_places=2)

