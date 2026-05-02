from rest_framework import serializers
from teacherapp.models import *

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherInfo
        fields = '__all__'