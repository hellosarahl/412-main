from django.urls import path
from .views import(MakeupListView, MakeupDetailView,CustomerDetailView,CustomerListView,
                   OrderDetail, OrderListView, create_order, add_item,delete,home)

"""Name:Sarah Lam 
File:urls.py
Description:"urls for the project """

urlpatterns=[
    #home page
    path("",home,name="home"),

    #customer page
    path("customers/",CustomerListView.as_view(),name="customerlist"),
    path("customers/<int:pk>/",CustomerDetailView.as_view(),name="customer"),


    #makeup pages
    path("makeup/",MakeupListView.as_view(), name="makeuplist"),
    path("makeup/<int:pk>/",MakeupDetailView.as_view(), name="makeup"),

    #order 
    path("orders/",OrderListView.as_view(),name="orderlist"),
    path("orders/<int:pk>/",OrderDetail.as_view(),name="order_detail"),
    path("orders/<int:pk>/delete/",delete,name="delete"),

    #forms
    path("orders/add_item/",add_item,name="add_item"),
    path("orders/create/",create_order,name="createorder")
    

]