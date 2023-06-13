from django.db import models


# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    """.vscode"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()
    expiry_date = models.DateField(blank=True, editable=True)

    def __str__(self):
        return str(self.name)


class Sale(models.Model):
    """.vscode"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    buyer = models.CharField(max_length=100)

    def __str__(self):
        return str(self.buyer)
