from django.contrib import admin

from .models import Product, Picture, Order, OrderLine


class PictureInline(admin.StackedInline):
    model = Picture


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "quantity"]
    list_editable = ["price", "quantity"]
    inlines = [PictureInline]


class OrderLineInline(admin.TabularInline):
    model = OrderLine


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderLineInline]
