from django.db import models
# from django.db.models import Model

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(
        verbose_name="Description of the product",
        null = False,
        blank = False
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    

class Order(models.Model):
    ORDER_STATUS_PENDING = 'P'
    ORDER_STATUS_COMPLETE = 'C'
    ORDER_STATUS_FAILED = 'F'
    ORDER_STATUS_CHOICES = [
        (ORDER_STATUS_PENDING, 'Pending'),
        (ORDER_STATUS_COMPLETE, 'Complete'),
        (ORDER_STATUS_FAILED, 'Failed')
    ]
    user_name = models.CharField(max_length=255, unique=True)
    total_cost = models.DecimalField(max_digits=6, decimal_places=2)
    date_of_submission = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=1, choices=ORDER_STATUS_CHOICES, default=ORDER_STATUS_PENDING)
    