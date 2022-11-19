from django.db import models
from base.models import User
# Create your models here.

class News(models.Model):
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']  
    