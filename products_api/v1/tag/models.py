from django.db import models

from products_api.mixins import TimeStampedMixin


class Tag(TimeStampedMixin):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name
