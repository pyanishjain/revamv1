from django.contrib import admin
from django.urls import path
from Shop.views import *

urlpatterns = [
    path('', index, name="shophome"),
    path('Fruit_page/', Fruits_page, name="Fruit_page"),
    path('Grocery_page/', Grocery_page, name="Grocery_page"),
    path('Vegetables_page/', Vegetables_page, name="Vegetables_page"),
    path('vendors/', vendors, name="vendors"),
    path('contactus/', contactus, name="contactus"),
    path('tracker/', tracker, name="tracker"),
    path('search/', search, name="search"),
    path('charity/', charity, name="charity"),
    path('checkout/', checkout, name="checkout"),
    path('handlerequest/', handlerequest, name="handlerequest"),
]