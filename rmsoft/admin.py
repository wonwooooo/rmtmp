from django.contrib import admin


# Register your models here.
from .models import Company, Client, Product, Order


admin.site.register(Company)
admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Order)