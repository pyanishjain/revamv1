from django.shortcuts import render
from .models import *
from math import ceil
import json
from django.views.decorators.csrf import csrf_exempt
# from Shop.payTm import Checksum
# Create your views here.
from django.http import HttpResponse
MERCHANT_KEY = 'rDiG9qWiL1v@%C1G'

# Create your views here.


def Fruits_page(request):
    all_fruits = Product.objects.filter(category="Fruits")
    alf = {
        "all_fruits":all_fruits
    }
    return render(request, 'Shop/Fruits..html', alf)

def Vegetables_page(request):
    all_vegetables = Product.objects.filter(category="Vegetables")
    alf = {
        "all_vegetables":all_vegetables
    }
    return render(request, 'Shop/Vegetables.html', alf)


def Grocery_page(request):
    all_grocery = Product.objects.filter(category="Grocery")
    alf = {
        "all_grocery":all_grocery
    }
    return render(request, 'Shop/Grocery.html', alf)


def dashboard(request):
    if request.method=="POST":
        product_name = request.POST('name', '')





def index(request):
    grocer = Product.objects.filter(category="Grocery")
    fruit = Product.objects.filter(category="Fruits")
    elc = Product.objects.filter(category="Vegetables")
    params ={"grocer":grocer, "fruit":fruit, "elc":elc}
    d = {"allproduct":params}
    return render(request, 'Shop/index.html', params,d)


def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone, amount=amount)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        thank = True
        id = order.order_id
        # return render(request, 'shop/checkout.html', {'thank':thank, 'id': id})
        # Request paytm to transfer the amount to your account after payment by user
        param_dict = {

                'MID': 'nVFsNy33180274639478',
                'ORDER_ID': str(order.order_id),
                'TXN_AMOUNT': str(amount),
                'CUST_ID': email,
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL':'http://127.0.0.1:8000/Shop/handlerequest/',

        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, 'Shop/paytm.html', {'param_dict': param_dict})

    return render(request, 'Shop/checkout.html')

@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'Shop/paymentstatus.html', {'response': response_dict})

def vendors(request):
    return render(request, "Shop/vendors.html")

def contactus(request):
    return HttpResponse("shoping page")

def tracker(request):
    return HttpResponse("shoping page")


def charity(request):
    return render(request, 'Shop/Charity.html')

def search(request):
    return  HttpResponse("you are on search")




