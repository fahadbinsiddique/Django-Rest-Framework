from django.db import models

# Create your models here.
class StudentInfo(models.Model):
    name=models.CharField(max_length=120,null=True)
    adress=models.CharField(max_length=120,null=True)
    department=models.CharField(max_length=120,null=True)
    gurdian_name=models.CharField(max_length=120,null=True)

    def __str__(self):
        return f'{self.name}'