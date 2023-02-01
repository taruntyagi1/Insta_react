from django.urls import path
from . import views
from products.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/',ProductView.as_view(),name='api'),
    
    path('variant/',ProductVariantList.as_view(),name = "variant"),
    path('api-category/',CategoryView.as_view()),
    path('variants/<int:product_id>/',VariantView.as_view()),
    path('add/<int:product_id>/<int:variant_id>/',views.add_to_cart,name='add'),
    path('login/',views.login_view,name='login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('product/<int:product_id>/',SingleProduct.as_view(),name='product'),
    path('variants/',AllVariants.as_view()),
    path('cart/',CartView.as_view()),
    path('usercart/',cartview.as_view())
    
   
]
