from django.urls import re_path, include
from rest_framework.routers import DefaultRouter

from v1.tag.views import TagViewSet

router = DefaultRouter()

router.register('tags', TagViewSet, basename='tags')

urlpatterns = [
    re_path(r'^', include(router.urls))
]
