from django.shortcuts import render,HttpResponse
from rest_framework.generics import ListCreateAPIView
from products.models import *
from products.serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework import generics

# Create your views here.



class ProductView(ListCreateAPIView):
    queryset = Product.objects.filter(is_active = True)
    serializer_class = ProductSerializer


class VariantView(APIView):

    def get(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
            variants = Variant.objects.filter(product=product)
            serializer = VariantSerializer(variants, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"error": "Product not found."}, status=status.HTTP_404_NOT_FOUND)

    


class CategoryView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer 
    

    
class CartView(ListCreateAPIView):
    queryset =  Cart.objects.all()
    serializer_class = CartSerializer



class ProductVariantList(generics.ListAPIView):
    queryset = Variant.objects.all()
    serializer_class = VariantSerializer
    def get_queryset(self):
        product_id = self.kwargs['product_id']
        return self.queryset.filter(product_id=product_id)

