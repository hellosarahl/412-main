from django.db import models

# Create your models here.
'''Models for my app for finding makeup
Name:Sarah Lam
file: models.py
'''


'''data model makeup'''
class Makeup(models.Model):
    name=models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/')
    price=models.DecimalField(max_digits=8,decimal_places=2)

    def __str__(self):
        return self.name
    
'''data model class for customers'''
class Customer(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    dateofbirth=models.DateField()
    address=models.CharField(max_length=100)


    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    

'''data model for order'''

class Order(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    status=models.CharField(max_length=100)
    dateoforder=models.DateField()

    def __str__(self):
        return f"Order{self.id}"
    
'''models for itemorder'''
class ItemOrder(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity= models.IntegerField()
    product= models.ForeignKey(Makeup, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.product.name}"


