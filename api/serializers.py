from rest_framework import serializers
from profiles.models import Profile
from order.models import Order
from products.models import Product


class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user']

class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['']

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['']


