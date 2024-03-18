from django.urls import path
from accounts.views import login_page
from accounts.views import signup_page
from products.views import add_to_cart
from products.views import cart
from products.views import remove_cart


urlpatterns = [
    path('login/', login_page , name = 'login'),
    path('signup/', signup_page, name = 'signup'),
    path('add_to_cart/<uid>/', add_to_cart, name = 'add_to_cart'),
    path('cart/', cart, name = 'cart'),
    path('remove_cart/<cart_item_uid>/', remove_cart, name = 'remove_cart'),
]