from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone_number']
    list_display_links = ['id', 'name', 'phone_number']

    prepopulated_fields = {
        'slug': ['name']
    }

    ordering = ['-public_date']

admin.site.register(Post, PostAdmin)