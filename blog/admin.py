from django.contrib import admin
from .models import Post
from .models import Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'author',
        'is_published',
        'created_at',
        'updated_at'
    ]
    list_filter = [
        'is_published',
        'created_at',
        'updated_at'
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'post',
        'author',
        'content',
        'is_published',
        'created_at'
    ]
    list_filter = [
        'is_published',
        'created_at'
    ]
