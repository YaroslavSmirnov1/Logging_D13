from django.shortcuts import render
from .models import Product
import logging

logger = logging.getLogger(__name__)


def index(request):
    product = Product.objects.all()
    return render(request, 'mc_donalds/products.html', context={'product': product})
