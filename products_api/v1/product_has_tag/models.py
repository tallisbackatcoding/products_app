from django.db import models

from products_api.mixins import TimeStampedMixin


class ProductHasTag(TimeStampedMixin):
    product = models.ForeignKey(
        'product.Product',
        on_delete=models.CASCADE
    )
    tag = models.ForeignKey(
        'tag.Tag',
        on_delete=models.CASCADE
    )
    def __str__(self):
        return str(self.product) + ' - ' + str(self.tag)
