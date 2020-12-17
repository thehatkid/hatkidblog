from django.db import models


class Post(models.Model):
    title = models.CharField(
        max_length=64,
        default="Sample Title...",
        verbose_name="Post's Title"
    )
    content = models.TextField(
        default="Sample Text...",
        verbose_name="Post's Text"
    )
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    is_published=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def get_absolute_url(self):
        return f"/post/{self.id}"
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']
