from django.urls import path

app_name = 'product'

urlpatterns = [
    path('products/', add_products_view, name='add'),
    path('products/<int:pk>/detail', get_products_view, name='get'),
    path('products/<int:pk>/update', update_products_view, name='update'),
    path('products/<int:pk>/delete', delete_products_view, name='delete')
]
