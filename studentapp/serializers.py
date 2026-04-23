from rest_framework import serializers
from studentapp.models import StudentInfo


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInfo
        fields = "__all__"
