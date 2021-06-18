from django.db import models


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
