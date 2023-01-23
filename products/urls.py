from django.urls import path
from . import views
from products.views import *

urlpatterns = [
    path('api/',ProductView.as_view(),name='api'),
    path('api/variants',VariantView.as_view()),
    path('api-category',CategoryView.as_view())
]
