from django.contrib import admin

from .models import Makeup, Customer, Order,ItemOrder


# Register your models here.

#register admin for makeup
admin.site.register(Makeup)
#register admin for customer
admin.site.register(Customer)
#register for order
admin.site.register(Order)
#register for item order
admin.site.register(ItemOrder)