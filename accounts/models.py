from django.db import models
from django.contrib.auth.models import User
from base.models import BaseModel
from products.models import Product
from products.models import Size, Quantity

class Profile(BaseModel):
    user  = models.OneToOneField(User, on_delete = models.CASCADE, related_name = "profile")

    def get_cart_count(self):
       return CartItems.objects.filter(cart__is_paid = False, cart__user = self.user).count()


class ProductCustomization(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "customization")
    is_paid = models.BooleanField(default = False)
    product_name = models.TextField(max_length = 150, null = True)
    size = models.TextField(max_length = 50, null = True)
    quantity = models.TextField(max_length = 50, null = True)
    nighty_length = models.TextField(max_length = 50)
    sleeve_type = models.TextField(max_length = 50)
    feeding_type = models.TextField(max_length = 50)
    zip_type = models.TextField(max_length = 50)


class Cart(BaseModel):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "carts")
    is_paid = models.BooleanField(default = False)
    


class CartItems(BaseModel):
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE, related_name = "cart_items")
    product = models.ForeignKey(Product, on_delete = models.SET_NULL, null = True, blank = True)
    size = models.ForeignKey(Size, on_delete = models.SET_NULL, null = True, blank = True,  related_name = "cart_items_size")
    quantity = models.ForeignKey(Quantity, on_delete = models.SET_NULL, null = True, blank = True,  related_name = "cart_items_quantity")
