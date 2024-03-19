from django.urls import path
from products.views import get_products
from products.views import maternity
from products.views import kaftan
from products.views import threebyfourth_sleeve
from products.views import search

urlpatterns = [
    path('<slug>', get_products, name = 'get_products'),
    path('maternity/', maternity, name = 'maternity'),
    path('kaftan/', kaftan, name = 'kaftan'),
    path('threebyfourth_sleeve/', threebyfourth_sleeve, name = 'threebyfourth_sleeve'),
    path('search/', search, name = 'search'),
]