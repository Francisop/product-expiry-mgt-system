from django.contrib import admin
from productManagement.models import Product, Category, Sale
# Register your models here.


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Sale)