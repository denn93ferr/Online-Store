from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit, Thumbnail


class Product(models.Model):
    title = models.CharField(_("title"), max_length=255)
    description = models.TextField(_("description"), null=False, blank=False)
    price = models.DecimalField(_("price"), max_digits=6, decimal_places=2)
    quantity = models.IntegerField(_("quantity"), default=0)

    class Meta:
        db_table = "products"
        verbose_name = _("product")
        verbose_name_plural = _("products")

    def __str__(self):
        return self.title


class Picture(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="pictures"
    )
    caption = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to="products")
    is_cover = models.BooleanField(default=False)
    image_large = ImageSpecField(
        source="image",
        processors=[ResizeToFit(800, 600)],
        format="JPEG",
        options={"quality": 70},
    )
    image_medium = ImageSpecField(
        source="image",
        processors=[ResizeToFit(480, 320)],
        format="JPEG",
        options={"quality": 70},
    )
    image_small = ImageSpecField(
        source="image",
        processors=[ResizeToFit(240, 160)],
        format="JPEG",
        options={"quality": 70},
    )
    image_thumb = ImageSpecField(
        source="image",
        processors=[Thumbnail(width=100, height=100)],
        format="JPEG",
        options={"quality": 70},
    )

    class Meta:
        db_table = "pictures"


class Order(models.Model):
    ORDER_STATUS_PENDING = "P"
    ORDER_STATUS_COMPLETE = "C"
    ORDER_STATUS_FAILED = "F"
    ORDER_STATUS_CHOICES = [
        (ORDER_STATUS_PENDING, "Pending"),
        (ORDER_STATUS_COMPLETE, "Complete"),
        (ORDER_STATUS_FAILED, "Failed"),
    ]
    order_status = models.CharField(
        max_length=1, choices=ORDER_STATUS_CHOICES, default=ORDER_STATUS_PENDING
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="orders",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "orders"

    @property
    def total(self):
        return sum(line.amount for line in self.lines.all())


class OrderLine(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="lines")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        db_table = "orderlines"

    @property
    def amount(self):
        return self.product.price * self.quantity
