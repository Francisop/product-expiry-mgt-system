from django.urls import path, reverse
from productManagement.views import Index, Inventory, AddProduct, Report, SaleView, product_detail, MakeSaleView

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('inventory/', Inventory.as_view(), name='inventory'),
    path('add-product/', AddProduct.as_view(), name='add-product'),
    path('Sale/all/', SaleView.as_view(), name='sale'),
    path('Sale/new/', MakeSaleView.as_view(), name='make-sale'),
    path('report/', Report.as_view(), name='report'),
    path('inventory/<int:product_id>/', product_detail, name='product_detail'),
]
