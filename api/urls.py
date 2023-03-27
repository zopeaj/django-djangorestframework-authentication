from django.urls import path
from api.views import ProfilesCreateAPIView, ProfileDetailAPIView, OrderList, OrderDetail, ProductDetail, ProductList

app_name = "api"

urlpatterns = [
    path('user/create', , name='create-user'),
    path('user/update', , name='update-user'),
    path('user/<int:pk>/', , name='get-user'),
    path('product/create', , name='create-product'),
    path('product/update', , name='update-product'),
    path('product/<int:pk>/', , name='get-product'),
    path('order/create', , name='create-order'),
    path('order/update', , name='update-order'),
    path('order/<int:pk>/', , name='get-order')
]


