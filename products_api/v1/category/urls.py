from django.urls import re_path, include
from rest_framework.routers import DefaultRouter

from v1.category.views import CategoryViewSet

router = DefaultRouter()

router.register('categories', CategoryViewSet, basename='category')

urlpatterns = [
    re_path(r'^', include(router.urls))
]
