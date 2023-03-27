from django.db import models
from django.url import reverse
from profiles.models import Profiles
from products.models import Product

# Create your models here.
class Order(models.Model):
    id = models.IntegerField(primary_key=True)
    product = models.OneToMany(Product, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_add_now=True)
    updated = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(Profiles, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('order:main', pk: self.kwargs['pk'])

    def __str__(self):
        return f"{self.user.username} - {self.datetime}"

