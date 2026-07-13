from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Article(models.Model):
    title = models.CharField()
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = [
            ('can_publish_article','Can publish article'),
        ]

    def __str__(self):
        return self.title