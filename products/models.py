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
    size = models.CharField(max_length = 100)

class Quantity(BaseModel):
    quantity = models.IntegerField()

class ProductCustomization(models.Model):
    Nighty_Length_choices = [
        ('30', '30'),
        ('31', '31'),
        ('32', '32'),
        ('33', '33'),
        ('34', '34'),
        ('35', '35'),
        ('36', '36'),
        ('37', '37'),
        ('38', '38'),
        ('39', '39'),
        ('40', '40'),
        ('41', '41'),
        ('42', '42'),
        ('43', '43'),
        ('44', '44'),
        ('45', '45'),
        ('46', '46'),
        ('47', '47'),
        ('48', '48'),
        ('49', '49'),
        ('50', '50'),
        ('51', '51'),
        ('52', '52'),
        ('53', '53'),
        ('54', '54'),
        ('55', '55'),
        ('56', '56'),
    ]

    Sleeve_Type_Choices = [
        ('Normal', 'Normal'),
        ('With Sleeve', 'With Sleeve'),
    ]

    Feeding_Type_Choices = [
        ('Feeding', 'Feeding'),
        ('Non Feeding', 'Non Feeding'),
    ]

    Zip_Type_Choices = [
        ('Two Side Zip', 'Two Side Zip'),
        ('Without Zip', 'Without Zip '),
    ]

    nighty_length = models.IntegerField()
    sleeve_type = models.CharField(max_length = 100, blank=False, null=False)
    feeding_type = models.CharField(max_length = 100, blank=False, null=False)
    zip_type = models.CharField(max_length = 100, blank=False, null=False)

    def __str__(self):
        return f"Customization for Product Id: {self.id}"

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

