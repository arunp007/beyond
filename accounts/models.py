from django.db import models
from django.contrib.auth.models import User
from base.models import BaseModel
from products.models import Product
from products.models import SizeVariant

class Profile(BaseModel):
    user  = models.OneToOneField(User, on_delete = models.CASCADE, related_name = "profile")

    def get_cart_count(self):
       return CartItems.objects.filter(cart__is_paid = False, cart__user = self.user).count()
    

class Cart(BaseModel):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "carts")
    is_paid = models.BooleanField(default = False)
    


class CartItems(BaseModel):
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE, related_name = "cart_items")
    product = models.ForeignKey(Product, on_delete = models.SET_NULL, null = True, blank = True)
    size_variant = models.ForeignKey(SizeVariant, on_delete = models.SET_NULL, null = True, blank = True)

