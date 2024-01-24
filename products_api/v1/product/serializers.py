from rest_framework import serializers

from v1.product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    category = serializers.CharField(source='category.name')

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'tags', 'category')
