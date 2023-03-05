from django.contrib import admin

from .models import *

class AigerimAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'photo')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'content')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

admin.site.register(Aigerim, AigerimAdmin)
admin.site.register(Category, CategoryAdmin)

