from django.contrib import admin

# Register your models here.
from django.contrib import admin
from rango.models import Category, Page, PageAdmin, CategoryAdmin

admin.site.register(Page, PageAdmin)
admin.site.register(Category, CategoryAdmin)
