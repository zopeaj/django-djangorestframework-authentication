from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.PrimaryKeyField(primary_key=True)
    name = models.CharField(nullable=False, max_length="200")
    category = models.TextField(default=None)
    price = models.FloatField(default=0.0, help_text='in NGN naira #')
    tax = models.FloatField(default=0.5)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)



