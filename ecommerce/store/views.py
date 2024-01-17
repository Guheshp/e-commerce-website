from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request, 'sub/index.html')

def Store(request):
    return render(request, 'sub/store.html')

def cart(request):
    return render(request, 'sub/cart.html')

def Checkout(request):
    return render(request, 'sub/checkout.html')