from django.contrib import admin
from products.models import *

# Register your models here.
class custom_product(admin.ModelAdmin):
    list_display = ['category','title','stock_record','price','image','is_active']
    ordering = ('id',)

class custom_category(admin.ModelAdmin):
    list_display = ['category_name','image','is_active']
    ordering = ('id',)

class custom_variant(admin.ModelAdmin):
    list_display = ['product','title','stock_record','price','image','is_active']
    ordering = ('id',)

class custom_cart(admin.ModelAdmin):
    list_display = ['product','quantity']
admin.site.register(Category,custom_category)
admin.site.register(Product,custom_product)
admin.site.register(Variant,custom_variant)
admin.site.register(Cart)
