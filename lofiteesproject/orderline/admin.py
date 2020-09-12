from django.contrib import admin

# Register your models here.
from .models import OrderLine

admin.site.register(OrderLine)