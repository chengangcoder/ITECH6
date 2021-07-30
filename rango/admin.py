from django.contrib import admin

# Register your models here.
from django.contrib import admin
from rango.models import Category, Page, PageAdmin, CategoryAdmin
from rango.models import UserProfile

admin.site.register(Page, PageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(UserProfile)
