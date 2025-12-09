from django.shortcuts import render,redirect
from django.views.generic import DetailView, ListView
from .forms import OrderForm, ItemOrderForm
from .models import Makeup, Customer, Order, ItemOrder

# Create your views here.
"""Name:Sarah Lam 
File:views.py
Description: This file has the views for the application for makeup. The list and details for the models"""



#home page
def home(request):
    return render(request,"home.html")
#list of makeup products
class MakeupListView(ListView):
    model=Makeup
    template_name="makeuplist.html"
    context_object_name="makeuplist"

    #for filtering makeup based on what the user searches up
    def get_queryset(self):
        s=super().get_queryset()
        q=self.request.GET.get("q")
        if q:
            s=s.filter(name__icontains=q)
        return s 



#info on makeup item
class MakeupDetailView(DetailView):
    model=Makeup
    template_name="makeupdetail.html"
    context_object_name="makeup"

#the customers
class CustomerListView(ListView):
    model=Customer
    template_name="customerlist.html"
    context_object_name="customerlist"

#the list of all orders
class OrderListView(ListView):
    model=Order
    template_name="orderlist.html"
    context_object_name="orderlist"

#details of a customer
class CustomerDetailView(DetailView):
    model=Customer
    template_name="customerdetail.html"
    context_object_name="customer"

#order detail and item
class OrderDetail(DetailView):
    model=Order
    template_name="orderdetail.html"
    context_object_name="order"

    def get_context_data(self, **kwargs):
        order=self.object
        context=super().get_context_data(**kwargs)
        context["items"]=ItemOrder.objects.filter(order=order)
        return context 


# new order
def create_order(request):
    if request.method=="POST":
        f=OrderForm(request.POST)
        if f.is_valid():
            o=f.save()
            return redirect("order_detail",pk=o.pk)
    else:
        f=OrderForm()
    return render(request,"createorder.html",{"f":f})
    

#new item added to order
def add_item(request,order_id=None):
    if request.method=="POST":
        f=ItemOrderForm(request.POST)
        if f.is_valid():
            i=f.save()
            return redirect("order_detail",pk=i.order.pk)
        
    else:
        f=ItemOrderForm()
    return render(request, "add_item.html",{"f":f})


#deleting an order
def delete(request,pk):
    order=Order.objects.get(pk=pk)
    order.delete()
    return redirect("orderlist")

