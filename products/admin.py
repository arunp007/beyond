from django.contrib import admin
from .models import Product, ProductImage
from.models import *

admin.site.register(Category)

class ProductImageAdmin(admin.StackedInline):
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display = ['category','product_name',  'color', 'price', 'product_description']
    inlines = [ProductImageAdmin,]

@admin.register(SizeVariant)

class SizeVariantAdmin(admin.ModelAdmin):
    list_display = ['size_name']
    model = SizeVariant

admin.site.register(Product, ProductAdmin)

admin.site.register(ProductImage)