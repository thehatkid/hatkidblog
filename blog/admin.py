from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'is_published', 'created_at', 'updated_at'
    ]
    list_filter = [
        'is_published', 'created_at'
    ]
