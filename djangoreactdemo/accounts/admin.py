from django.contrib import admin
from .models import Products,Store


admin.site.register(Products)
admin.site.site_header = "Product Database"
admin.site.register(Store)
