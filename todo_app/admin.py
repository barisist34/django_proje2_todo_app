from django.contrib import admin
from .models import Todo,Category,Tag


class TodoAdmin(admin.ModelAdmin):
    list_display=[
        'id',
        'user',
        'category',
        #'tag',
        'title',
        'is_active',
        'created_at',
        'updated_at',
    ]
    list_display_links=[
        'id',
        'title',
        'created_at',

    ]

class CategoryAdmin(admin.ModelAdmin):
    list_display=[
        'title',
        'slug',
        'is_active',
    ]
    list_display_links=[
        'title',
        'slug',
        'is_active',
    ]

admin.site.register(Todo,TodoAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag)