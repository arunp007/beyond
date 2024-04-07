from django.contrib import admin
from.models import Profile, CartItems, Cart
from.models import ProductCustomization


class ProductCustomizationAdmin(admin.ModelAdmin):
    list_display = ('user','product_name','size', 'quantity', 'nighty_length','sleeve_type', 'feeding_type', 'zip_type')
    model = ProductCustomization

class CartItemsAdmin(admin.ModelAdmin):
    list_display = ('product','size', 'quantity')

class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_paid')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)

admin.site.register(Profile, ProfileAdmin)

admin.site.register(ProductCustomization, ProductCustomizationAdmin)

admin.site.register(Cart, CartAdmin)

admin.site.register(CartItems, CartItemsAdmin)

