from rest_framework import serializers
from departmentapp.models import *

class departmentSerailizer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentModel
        fields= '__all__'