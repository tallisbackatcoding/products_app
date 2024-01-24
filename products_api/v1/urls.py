from django.urls import re_path, include

app_name = 'v1'

urlpatterns = [
    re_path(r'^', include('v1.product.urls')),
    re_path(r'^', include('v1.category.urls')),
    re_path(r'^', include('v1.tag.urls'))
]
