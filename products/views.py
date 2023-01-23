from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from products.models import *
from products.serializers import *
from rest_framework.response import Response
from rest_framework import status

# Create your views here.



class ProductView(ListCreateAPIView):
    queryset = Product.objects.filter(is_active = True)
    serializer_class = ProductSerializer


class VariantView(ListCreateAPIView):
    queryset = Variant.objects.all()
    serializer_class = VariantSerializer


class CategoryView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer 
    

    
