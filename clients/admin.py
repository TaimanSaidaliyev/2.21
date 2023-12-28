from django.contrib import admin
from .models import *

admin.site.register([Clients, Categories, Hobbies])