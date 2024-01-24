from django.contrib import admin

# Register your models here.
from v1.product.models import Product


class ProductAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags', )


admin.site.register(Product, ProductAdmin)
