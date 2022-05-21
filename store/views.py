from django.views.generic import ListView, TemplateView
from .models import Product


class ListProducts(ListView):
    model = Product
    template_name = "list_products.html"


class HomeView(TemplateView):
    template_name = "home.html"


# def all_products(request):
