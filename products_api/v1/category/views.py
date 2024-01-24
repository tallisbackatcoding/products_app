from rest_framework import viewsets

from v1.category.models import Category
from v1.category.serializers import CategorySerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects
    serializer_class = CategorySerializer
