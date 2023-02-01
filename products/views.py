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
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login,logout,authenticate
import jwt
from django.http import JsonResponse
import json
from django.conf  import settings
import datetime
from rest_framework.decorators import api_view

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
@csrf_exempt
def add_to_cart(request,product_id,variant_id):
    user = request.user.id
    product = Product.objects.get(id = product_id)
    variant = Variant.objects.get(id = variant_id)
    cart, created = Cart.objects.get_or_create(product = product,user = user)
    cart_item, created = cartitem.objects.get_or_create(cart = cart,product = product,variant = variant)
    cart_item.quantity = 1
    cart_item.save()
    if cart_item.product is not None:
        cart_item.quantity += 1
        cart_item.save()
    return HttpResponse(cart_item)

@csrf_exempt
@api_view(['POST'])
def login_view(request):
    
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request,email = email,password = password)
        if user is not None:
            paylod = {
                'id' : user.id,
                'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=60)
            } 
            token = jwt.encode(paylod, 'secret', algorithm='HS256')
            response = Response()
            response.set_cookie(key='jwt', value=token,httponly=True)
            response.data = {
                'jwt' : token,
              
               
            }
            return response
        else:
                return JsonResponse({
                    'message' : 'invalid request'
                })
class SingleProduct(ListCreateAPIView):
    # def get(self,request,product_id):
    #     product = Product.objects.get(id = product_id)
    #     serializer = ProductSerializer(product).data
    #     return Response(serializer,status=status.HTTP_202_ACCEPTED)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        return self.queryset.filter(id=product_id)


            
        
            
class AllVariants(APIView):
    def get(self,request):
        variant = Variant.objects.all()
        serializer = VariantSerializer(variant,many = True).data
        return Response(serializer,status=status.HTTP_200_OK)       
    
            

class cartview(APIView):
    def get(self,request):
        user = request.user
        cart = Cart.objects.get(user = user.id)
        serializer = CartSerializer(cart).data
        return Response(serializer,status=status.HTTP_200_OK)
        

