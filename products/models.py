from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    sku = models.CharField(max_length=254, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    lash_length_and_curl = models.CharField(max_length=254)
    lash_line_length = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField()

    def __str__(self):
        return self.name


class ProductReview(models.Model):
    product = models.ForeignKey(
        Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name='reviews', on_delete=models.CASCADE)
    content = models.TextField(blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
