from django.db import models

# Create your models here.


class Product(models.Model):
    """.vscode"""
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()
    expiry_date = models.DateTimeField(blank=True,editable=True,)
    Price = models.IntegerField()

    def __str__(self):
        return str(self.name)