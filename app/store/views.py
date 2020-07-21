from django.shortcuts import render
from .models import *

def store(request):
    """render all the products"""

    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'store/store.html', context)

def cart(request):
    """render cart items here"""

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
    context = {'items':items, 'order':order}
    return render(request, 'store/cart.html', context)

def checkout(request):
    """render the checkout page with product summary"""
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
    context = {'items':items, 'order':order}
    return render(request, 'store/checkout.html', context)
