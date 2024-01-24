from django.db import models

from products_api.mixins import TimeStampedMixin


class Category(TimeStampedMixin):
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name = 'categories'

    def __str__(self):
        return self.name
