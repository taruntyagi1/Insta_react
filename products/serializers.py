from rest_framework import serializers
from products.models import *

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'category_name','slug','image','description','is_active','is_featured','is_public'
        )

class VariantSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Variant
        fields = (
            'product','title','slug','stock_record','description','price','image','is_active','is_featured','is_public'
        )

class ProductSerializer(serializers.ModelSerializer):
    
    category = CategorySerializer()
    class Meta:
        model  = Product
        fields = (
          'category',"title",'slug','stock_record','description','price','image','is_active','is_featured','is_public',
        )

