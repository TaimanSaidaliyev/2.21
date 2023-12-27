from django.urls import path
from .views import *


urlpatterns = [
    path('',  view_products, name='view_products'),
    path('add',  add_product, name='add_product'),
    path('detail/<int:product_id>',  view_detail_product, name='view_detail_product'),
    path('remove/<int:product_id>',  delete_product),
]