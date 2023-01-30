from django.urls import path
from . import views
from products.views import *

urlpatterns = [
    path('api/',ProductView.as_view(),name='api'),
    
    path('variant/',ProductVariantList.as_view(),name = "variant"),
    path('api-category',CategoryView.as_view()),
    path('variants/<int:product_id>/',VariantView.as_view()),
    path('add/<int:product_id>/<int:variant_id>/',views.add_to_cart,name='add'),
    
   
]
