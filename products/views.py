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
    

    
class CartView(ListCreateAPIView):
    queryset =  Cart.objects.all()
    serializer_class = CartSerializer


def get_variants(request,product_id):
    variant = Variant.objects.filter(id=product_id)
    return Response(variant,status=status.HTTP_202_ACCEPTED)
