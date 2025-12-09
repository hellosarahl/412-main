from django import forms
from .models import Order, ItemOrder
"""Name:Sarah Lam 
File:forms.py
Description: This file is a form for makeup order application. Allows the user to add orders and 
have new orders
"""

#form for creating new orders 
class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields= ["customer","dateoforder", "status"]

#adding product to an order there already is
class ItemOrderForm(forms.ModelForm):
    class Meta:
        model=ItemOrder
        fields=["product","quantity","order"]