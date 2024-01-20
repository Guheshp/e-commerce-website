from django.urls import path

from . import views

urlpatterns = [

    path('', views.Home, name='my-home'),
    path('store', views.Store, name='my-store'),
    path('cart', views.cart, name='my-cart'),
    path('checkout', views.Checkout, name='my-checkout'),
    path('updateitem', views.UpdateItem, name='my-updateitem'),
    path('process_order', views.ProcessOrder, name='my-process_order'),

]