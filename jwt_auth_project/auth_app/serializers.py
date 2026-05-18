from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import *

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username','email','password','confirm_password']
    
    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise ValidationError('password do not match')
        return data 
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user= User.objects.create_user(**validated_data)
        return user
    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(
            username=data['username'],
            password=data['password']
        )

        if not user:
            raise ValidationError("Invalid credentials")

        data['user'] = user
        return data
    
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model= StudentModel
        fields= '__all__'