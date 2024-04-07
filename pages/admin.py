from django.contrib import admin
from pages.models import Contact_us

class Contact_usAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message')
    model = Contact_us

admin.site.register(Contact_us, Contact_usAdmin)

