from django.contrib import admin
from.models import Profile, CartItems, Cart
from.models import ProductCustomization, Variant


class ProductCustomizationAdmin(admin.ModelAdmin):
    list_display = ('user','product_name','size', 'quantity', 'nighty_length','sleeve_type', 'feeding_type', 'zip_type')
    model = ProductCustomization

class VariantAdmin(admin.ModelAdmin):
    list_display = ('user', 'size', 'quantity')
    model = Variant

class CartItemsAdmin(admin.ModelAdmin):
    list_display = ('product',)

class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_paid')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)

admin.site.register(Profile, ProfileAdmin)

admin.site.register(ProductCustomization, ProductCustomizationAdmin)

admin.site.register(Variant, VariantAdmin)

admin.site.register(Cart, CartAdmin)

admin.site.register(CartItems, CartItemsAdmin)

