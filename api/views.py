from django.shortcuts import render
from rest_framework.views.decorator import api_view
from rest_framework.response import Response
from rest_framework.request import Request

# Create your views here.

@api_view(['POST'])
def add_order(request):
    pass

@api_view(['GET'])
def get_order(request):
    pass

@api_view(['PUT'])
def update_order(request):
    pass

@api_view(['DELETE'])
def delete_order(request):
    pass


@api_view(['POST'])
def add_product(request):
    pass

@api_view(['GET'])
def get_product(request):
    pass

@api_view(['PUT'])
def update_product(request):
    pass

@api_view
def delete_product(request):
    pass

