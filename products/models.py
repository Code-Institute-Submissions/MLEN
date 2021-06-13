from django.db import models

# Create your models here.


class Product(models.Model):
    sku = models.CharField(max_length=254, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    lash_length_and_curl = models.TextField(blank=True)
    lash_line_length = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField()

    def __str__(self):
        return self.name
