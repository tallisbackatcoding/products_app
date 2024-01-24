from django.urls import re_path, include
from rest_framework.routers import DefaultRouter

from v1.product.views import ProductViewSet

router = DefaultRouter()

router.register('products', ProductViewSet, basename='products')

urlpatterns = [
    re_path(r'^', include(router.urls))
]