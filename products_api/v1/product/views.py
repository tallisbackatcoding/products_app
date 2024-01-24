from django.db.models import Q
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

from v1.product.models import Product
from v1.product.serializers import ProductSerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects
    pagination_class = LimitOffsetPagination
    serializer_class = ProductSerializer

    def get_queryset(self):
        # All Description, tags and category returned inside list view
        # to demonstrate the usage of select_related and prefetch_related
        queryset = self.queryset.select_related('category').prefetch_related('tags')
        filter_args = dict()
        if self.request.query_params.get('category'):
            filter_args['category'] = self.request.query_params.get('category')
        if self.request.query_params.get('tags'):
            tags = self.request.query_params.get('tags').split(',')
            filter_args['tags__in'] = tags
        queryset = queryset.filter(**filter_args)
        search_text = self.request.query_params.get('search')
        if search_text and len(search_text) >= 2:
            queryset = queryset.filter(
                Q(Q(name__icontains=search_text) | Q(description__icontains=search_text))
            )
        return queryset
