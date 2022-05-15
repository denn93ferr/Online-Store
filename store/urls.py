from typing import List
from django.urls import path
from .views import ListProducts, HomeView


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("products/", ListProducts.as_view(), name="products"),
]
