from django.urls import path
from productManagement.views import Index,Inventory
# from note.views import (AboutUs, Index, NoteView, PrintView)

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('inventory/', Inventory.as_view(), name='index'),
]
