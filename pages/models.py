from django.db import models

class Contact_us(models.Model):
    name = models.TextField(max_length = 100)
    email = models.TextField(max_length = 100)
    phone = models.TextField(max_length = 100)
    message = models.TextField(max_length = 200)
    
