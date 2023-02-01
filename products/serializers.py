from rest_framework import serializers
from products.models import *

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'id','category_name','slug','image','description','is_active','is_featured','is_public'
        )



class VariantSerializer(serializers.ModelSerializer):
    
   
    class Meta:
        model = Variant
        fields = (
            'id','product','title','slug','stock_record','description','price','image','is_active','is_featured','is_public'
        )

    
    


        

class ProductSerializer(serializers.ModelSerializer):
    variant = serializers.SlugRelatedField(many = True,read_only = True,slug_field= 'title')
    category = CategorySerializer()
    class Meta:
        model  = Product
        fields = (
          'id','category','variant',"title",'slug','stock_record','description','price','image','is_active','is_featured','is_public',
        )

        def get_image_url(self,obj):
             return obj.image.url


class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Cart
        fields = (
            '__all__'
        )

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = (
            '__all__'
        )