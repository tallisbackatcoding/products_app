from django.db import models

from products_api.mixins import TimeStampedMixin
from v1.product_has_tag.models import ProductHasTag


class Product(TimeStampedMixin):
    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=256, null=True, blank=True)
    category = models.ForeignKey(
        'category.Category',
        on_delete=models.SET_NULL,
        null=True
    )
    tags = models.ManyToManyField(
        'tag.Tag',
        through=ProductHasTag,
        related_name='products'
    )

    def __str__(self):
        return self.name
