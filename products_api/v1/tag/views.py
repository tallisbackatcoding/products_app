from rest_framework import viewsets

from v1.tag.models import Tag
from v1.tag.serializers import TagSerializer


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects
    serializer_class = TagSerializer
