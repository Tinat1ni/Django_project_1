from django.urls import path
from .views import home, category, product_detail, contact

app_name = 'store'
urlpatterns = [
    path('', home, name='home'),
    path('category/<slug:slug>/', category, name='category'),
    path('product/<slug:slug>/', product_detail, name='product'),
    path('contact', contact, name='contact')
]