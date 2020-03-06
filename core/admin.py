from django.contrib import admin
from .models import Item, Category

# Register your models here.
from .models import Item, Category

admin.site.register(Item)
admin.site.register(Category)