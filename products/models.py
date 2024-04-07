from django.db import models
from base.models import BaseModel
from django.utils.text import slugify

class Category(BaseModel):
    category_name = models.CharField(max_length = 100)
    slug = models.SlugField(unique = True, null = True, blank = True)
    category_images = models.ImageField(upload_to="categories")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.category_name
    
class SizeVariant(BaseModel):
    size_name = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.size_name

class Size(BaseModel):
    size = models.CharField(max_length = 100, null = True)

class Quantity(BaseModel):
    quantity = models.IntegerField(null = True)


class Product(BaseModel):
    product_name = models.CharField(max_length = 100)
    slug = models.SlugField(unique = True, null = True, blank = True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name = "products")
    brand = models.CharField(max_length = 100, null = True)
    price = models.TextField(max_length = 10, null = True)
    dummy_price = models.TextField(max_length = 10, null = True)
    product_description = models.TextField(max_length = 500)
    color = models.CharField(max_length = 100, null = True)
    size_variant = models.ManyToManyField(SizeVariant, blank = True)
    in_stock = models.BooleanField(default = True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.product_name


class ProductImage(BaseModel):
    product = models.ForeignKey(Product,  on_delete = models.CASCADE, related_name = "product_images")
    image = models.ImageField(upload_to="product")

