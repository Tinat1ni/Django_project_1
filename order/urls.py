from django.urls import path
from .views import cartView, checkout

urlpatterns = [
    path('cart/', cartView, name='cart'),
    path('checkout/', checkout, name='checkout')
]
