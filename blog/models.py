from django.db import models
from django.contrib.auth.models import User


# Посты
class Post(models.Model):
    title = models.CharField(
        max_length=80,
        verbose_name="Заголовок поста",
        default="Untitled Post"
    )
    content = models.TextField(
        verbose_name="Контент поста",
        default="Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    )
    author = models.ForeignKey(
        User,
        verbose_name="Автор",
        on_delete=models.CASCADE
    )
    is_published = models.BooleanField(
        verbose_name="Публикация",
        default=False
    )
    created_at = models.DateTimeField(
        verbose_name="Создан",
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="Изменено",
        auto_now=True
    )
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f"/post/{self.id}/"
    
    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ['-created_at']


# Комментарии
class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        verbose_name="Пост",
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        User,
        verbose_name="Автор",
        on_delete=models.CASCADE,
        default=None
    )
    content = models.TextField(
        verbose_name="Текст"
    )
    is_published = models.BooleanField(
        verbose_name="Публикация",
        default=True
    )
    created_at = models.DateTimeField(
        verbose_name="Создан",
        auto_now_add=True
    )
    
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ['created_at']
