from django.urls import path
from .views import *


urlpatterns = [
    path('',  show_list_clients, name='view_clients'),
    path('detail/<int:client_id>',  client_detail, name='detail_client'),
]