from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('manager', 'Manager'),
        ('staff', 'Staff'),
    )

    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

    def __str__(self):
        return self.username
    
class StudentModel(models.Model):
    name = models.CharField(max_length=100,null=True)
    email= models.EmailField(null=True)
    address = models.TextField(null=True)