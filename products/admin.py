from django.contrib import admin
from .models import Product, ProductImage
from.models import *

admin.site.register(Category)

class ProductImageAdmin(admin.StackedInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    list_display = ('category','product_name',  'color', 'price', 'product_description', 'in_stock_display',)
    list_filter = ('in_stock', 'category',)
    search_fields = ('product_name', 'product_description',)
    action = ['mark_as_out_of_stock']
    inlines = [ProductImageAdmin,]
    
    def mark_as_out_of_stock(self, request, queryset):
        queryset.update(in_stock = False)
    mark_as_out_of_stock.short_description = "Mark selected products as out of stock"

    def in_stock_display(self, obj):
        return obj.in_stock
    in_stock_display.boolean = True

@admin.register(SizeVariant)

class SizeVariantAdmin(admin.ModelAdmin):
    list_display = ['size_name']
    model = SizeVariant


admin.site.register(Product, ProductAdmin)

admin.site.register(Size)

admin.site.register(Quantity)

admin.site.register(ProductImage)