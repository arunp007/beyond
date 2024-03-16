from django.urls import path
from accounts.views import login_page
from accounts.views import signup_page
from products.views import add_to_cart
from products.views import cart


urlpatterns = [
    path('login/', login_page , name = 'login'),
    path('signup/', signup_page, name = 'signup'),
    path('add_to_cart/<uid>/', add_to_cart, name = 'add_to_cart'),
    path('cart', cart, name = 'cart'),
]