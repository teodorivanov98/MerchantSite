
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('alcoholic', 'Alcoholic'),
        ('non-alcoholic', 'Non-Alcoholic'),
        ('water', 'Water'),
        ('beer', 'Beer'),
        ('juice', 'Juice'),
        ('carbonated', 'Carbonated'),
        ('keg', 'Keg'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name
