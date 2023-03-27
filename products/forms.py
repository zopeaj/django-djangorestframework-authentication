from django import forms
from products.models import Product


class ProductCreateForm(forms.FormModel):
    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'tax', 'created']

class ProductUpdateForm(forms.FormModel):
    class Meta:
        model = Product
        exclude = ['update']



