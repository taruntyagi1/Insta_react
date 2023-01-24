from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=1000,unique=True,blank=True)
    slug = models.SlugField(max_length=1000,unique=True,blank=True)
    image = models.FileField(upload_to='photo/category',blank =True)
    description = models.TextField(max_length=1000,blank = True)
    is_active = models.BooleanField(default=True)
    is_featured  = models.BooleanField(default=True)
    is_public  = models.BooleanField(default=True)


    def __str__(self):
        return self.category_name

def pre_save_product_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.category_name)

pre_save.connect(pre_save_product_receiver, sender=Category)


    


class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=100,unique=True,blank=True)
    slug = models.SlugField(max_length=1000,unique=True,blank=True)
    stock_record  = models.IntegerField(blank=True)
    description = models.TextField(max_length=1000,blank = True)
    image = models.FileField(upload_to='photo/products',blank=True)
    price = models.IntegerField(blank = True)
    is_active = models.BooleanField(default=True)
    is_featured  = models.BooleanField(default=True)
    is_public  = models.BooleanField(default=True)

    def __str__(self):
        return self.title


def pre_save_product_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)

pre_save.connect(pre_save_product_receiver, sender=Product)



class Variant(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    title = models.CharField(max_length=100,unique=True,blank=True)
    slug = models.SlugField(max_length=1000,unique=True,blank=True)
    stock_record  = models.IntegerField(blank=True)
    description = models.TextField(max_length=1000,blank = True)
    image = models.FileField(upload_to='photo/products',blank=True)
    price = models.IntegerField(blank = True)
    is_active = models.BooleanField(default=True)
    is_featured  = models.BooleanField(default=True)
    is_public  = models.BooleanField(default=True)

def pre_save_product_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)

pre_save.connect(pre_save_product_receiver, sender=Variant)



class Cart(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.CharField(max_length=100)
