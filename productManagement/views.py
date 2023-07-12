from django.shortcuts import render, redirect
from django.views import View
from datetime import date
from productManagement.models import Product, Sale, Category
from django.shortcuts import render, get_object_or_404


# Create your views here.


class Index(View):
    """.vscode"""
    template_name = "index.html"

    def get(self, request):
        """.vscode"""
        products = Product.objects.all()
        top_5 = products[:5]
        expired_products = []

        today = date.today()
        for product in products:
            if product.expiry_date < today:
                expired_products.append(product)
        context = {"today_now": today, 'product_count': len(list(products)), 'expired_products': expired_products,
                   'expired': len(expired_products), 'top_5': top_5}

        return render(request, self.template_name, context=context)


class Inventory(View):
    """.vscode"""
    template_name = "inventory.html"

    def get(self, request):
        inventory = Product.objects.all()
        expired_products = []

        today = date.today()
        for product in inventory:
            if product.expiry_date < today:
                expired_products.append(product)
        data = {"products": list(inventory), 'expired_products': expired_products, "today_now": today}
        print(data)
        return render(request, self.template_name, context=data)


def product_detail(request, product_id):
    if request.POST:
        print(product_id)
        product = get_object_or_404(Product, pk=product_id)
        product.delete()
        return redirect("inventory")
    else:
        product = get_object_or_404(Product, id=product_id)
        context = {
            'product': product,
            # Other context variables
        }
        return render(request, 'product_detail.html', context)




class AddProduct(View):
    """.vscode"""
    template_name = "add_product.html"

    def get(self, request):
        """.vscode"""
        category = Category.objects.all()
        context = {"categories": list(category)}
        return render(request, self.template_name, context)

    def post(self, request):
        name = request.POST.get('name')
        price = request.POST.get('price')
        quantity = request.POST.get('qty')
        description = request.POST.get('desc')
        expiry_date = request.POST.get('exp')
        category_id = int(request.POST.get('category'))
        category = Category.objects.get(pk=category_id)
        product = Product(category=category, name=name, price=price, quantity=quantity, description=description,
                          expiry_date=expiry_date)
        product.save()
        return redirect('inventory')  # 'inventory'


class SaleView(View):
    """.vscode"""
    template_name = "sale.html"

    def get(self, request):
        """.vscode"""
        sales = Sale.objects.all()

        context = {"sales": list(sales)}
        return render(request, self.template_name, context=context)


class MakeSaleView(View):
    """.vscode"""
    template_name = "make-sale.html"

    def get(self, request):
        """.vscode"""
        products = Product.objects.all()
        context = {
            'products': products
        }
        return render(request, self.template_name, context=context)

    def post(self, request):
        cust_name = request.POST.get("cust_name")
        cust_phone = request.POST.get("cust_phone")
        sale_data = request.POST.get("sale_data")
        print(cust_name)
        print(cust_phone)
        print(sale_data)
        sale_data = sale_data.split(',')

        for item in sale_data:
            if item:
                parts = item.split(' x ')
                item_name = parts[0]
                product = Product.objects.get(name=item_name)
                quantity = int(parts[1])
                # print(product)
                total =product.price * quantity
                print("Item:", item_name)
                print("Quantity:", quantity)
                print("total:", total)

                # reduce the total quantity
                if product.quantity < quantity:
                    context = {
                        'message': f'{product.name} has only {product.quantity} 12 left...try with a lesser number'
                    }
                    return  render(request, self.template_name, context=context)
                else:
                    product.quantity = product.quantity - quantity
                    product.save()
                    sale = Sale(product=product, quantity=quantity, buyer=cust_name, total=total,)
                    sale.save()

                print("-----")


        return redirect('/')


class Report(View):
    """.vscode"""
    template_name = "report.html"

    def get(self, request):
        """.vscode"""
        return render(request, self.template_name)
