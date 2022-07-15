from django.db import models


# Create your models here.
class Production(models.Model):
    product_name = models.CharField(max_length=200)
    amount_product = models.IntegerField(default=1)
    price = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=False)