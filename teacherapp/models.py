from django.db import models

# Create your models here.
class TeacherInfo(models.Model):
    name=models.CharField(max_length=120,null=True)
    adress=models.CharField(max_length=120,null=True)
    department=models.CharField(max_length=120,null=True)
    Phone= models.CharField(max_length=120,null=True)
    email=models.EmailField(max_length=120,null=True)
    def __str__(self):
        return f'{self.name}'