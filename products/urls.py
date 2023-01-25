from django.urls import path
from . import views
from products.views import *

urlpatterns = [
    path('api/',ProductView.as_view(),name='api'),
    path('variants/<int:product_id>/',VariantView.as_view(),name='variants'),
    path('variant/<int:product_id>/',ProductVariantList.as_view(),name = "variant"),
    path('api-category',CategoryView.as_view()),
    
   
]
