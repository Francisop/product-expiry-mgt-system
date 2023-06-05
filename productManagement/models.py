from django.db import models


# Create your models here.


class Product(models.Model):
    """.vscode"""
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()
    expiry_date = models.DateField(blank=True, editable=True)

    def __str__(self):
        return str(self.name)
