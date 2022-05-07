from django.views.generic import ListView
from .models import Product


class ListProducts(ListView):
    model = Product
    template_name = "list_products.html"
