from django import forms
from order.models import Order

class OrderCreateForm(models.FormModel):
    class Meta:
        model = Order
        exclude = ('user_id', 'updated')

class OrderUpdateForm(models.FormModel):
    class Meta:
        model = Order
        exclude = ('created', )
