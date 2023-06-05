from django.shortcuts import render, redirect
from django.views import View

from productManagement.models import Product


# Create your views here.


class Index(View):
    """.vscode"""
    template_name = "index.html"

    def get(self, request):
        """.vscode"""
        return render(request, self.template_name)


class Inventory(View):
    """.vscode"""
    template_name = "inventory.html"

    def get(self, request):
        inventory = Product.objects.all()
        data = {"products": list(inventory)}
        print(data)
        return render(request, self.template_name, context=data)


class AddProduct(View):
    """.vscode"""
    template_name = "add_product.html"

    def get(self, request):
        """.vscode"""
        return render(request, self.template_name)

    def post(self, request):
        name = request.POST.get('name')
        price = request.POST.get('price')
        quantity = request.POST.get('qty')
        description = request.POST.get('desc')
        expiry_date = request.POST.get('exp')
        product = Product(name=name, price=price, quantity=quantity, description=description, expiry_date=expiry_date)
        product.save()
        return redirect('inventory')  # 'inventory'


class Report(View):
    """.vscode"""
    template_name = "report.html"

    def get(self, request):
        """.vscode"""
        return render(request, self.template_name)
