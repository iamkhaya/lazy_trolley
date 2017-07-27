from django.shortcuts import render
from django.http import Http404

from inventory.models import Product

def index(request):
    products = Product.objects.all()
    return render(request, 'inventory/index.html', {
        'products':products,
    })
