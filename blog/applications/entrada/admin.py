from applications.entrada.models import Category, Entry, Tag
from django.contrib import admin

# Register your models here.

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Entry)
