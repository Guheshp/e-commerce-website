from django.shortcuts import render
from . models import (Products,Order,Customer,OrderItem,ShippingAddress )
from django.http import JsonResponse
import json
import datetime
# Create your views here.

def Home(request):
  
    return render(request, 'sub/index.html')

# store products.

def Store(request):

    if request.user.is_authenticated:

        customer = request.user.customer

        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items =[]
        order = {'get_cart_total': 0, 'get_cart_items': 0, }
        cartItems = order['get_cart_items']

    products = Products.objects.all()

    context = {'products' : products, 'cartItems':cartItems, }

    return render(request, 'sub/store.html', context)

# cart.

def cart(request):

    if request.user.is_authenticated:

        customer = request.user.customer

        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    else:

        items =[]
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']
 
    context = {'items': items, 'order':order, 'cartItems':cartItems}

    return render(request, 'sub/cart.html', context)

# checkout. 

def Checkout(request):

    if request.user.is_authenticated:

        customer = request.user.customer

        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items =[]
        order = {'get_cart_total': 0, 'get_cart_items': 0, }
        cartItems = order['get_cart_items']
 
    context = {'items': items, 'order':order,'cartItems':cartItems }

    return render(request, 'sub/checkout.html',context)

# UpdateItem.

def UpdateItem(request):

    data = json.loads(request.body)

    productId = data['productId']
    action = data['action']

    print('Action: ', action)
    print('ProductId: ', productId)

    customer = request.user.customer
    product = Products.objects.get(id=productId)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
         orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    
    return JsonResponse('item was added', safe=False )


def ProcessOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        if order.shipping == True:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],
               

            )

    else:
        print('user not logged in..')

    return JsonResponse('Payment Complete', safe=False )