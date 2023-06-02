from django.shortcuts import render
from django.views import View

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
        """.vscode"""
        return render(request, self.template_name)
