from django.urls import path
from productManagement.views import Index, Inventory, AddProduct, Report

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('inventory/', Inventory.as_view(), name='inventory'),
    path('add-product/', AddProduct.as_view(), name='add-product'),
    path('report/', Report.as_view(), name='report'),
]
