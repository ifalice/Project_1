from django.db import models

class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to = r'photos/%Y/%m/%d/')
    is_pablished = models.BooleanField(default=True) 

    def __str__(self):
        return self.title