from django.shortcuts import render, HttpResponse
from rest_framework.generics import ListCreateAPIView
from products.models import *
from products.serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework import generics
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

# Create your views here.


class ProductView(ListCreateAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer


class CategoryView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CartView(ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class VariantView(APIView):
    def get(self, request, product_id):
        product = Product.objects.get(id=product_id)
        variants = Variant.objects.filter(product=product)
        serializer = VariantSerializer(variants, many=True)
        return Response(serializer.data)


class ProductVariantList(generics.ListAPIView):
    queryset = Variant.objects.all()
    serializer_class = VariantSerializer
    # def get_queryset(self):
    #     product_id = self.kwargs['product_id']
    #     return self.queryset.filter(product__id=product_id)


# def product_detail(request, product_id):
#     product = get_object_or_404(Product, pk=product_id)
#     variants = Variant.objects.filter(product=product)
#     context = {
#         'product' : product,
#         'variants' : variants,
#     }
#     return render(request, 'variant.html',context)

def add_to_cart(request,product_id,variant_id):
    product = Product.objects.get(id = product_id)
    variant = Variant.objects.get(id = variant_id)
    cart, created = Cart.objects.get_or_create(user = request.user)
    cart_item, created = cartitem.objects.get_or_create(cart = cart,product = product,variant = variant)
    cart_item.quantity = 1
    cart_item.save()
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return HttpResponse(cart_item)
        

