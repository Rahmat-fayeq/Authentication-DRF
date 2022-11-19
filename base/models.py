from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # class Meta:
    #     ordering = ['-created_at','-updated_at']
    
class Rest_password(models.Model):
    email = models.EmailField(max_length=100)
    token = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.email
    