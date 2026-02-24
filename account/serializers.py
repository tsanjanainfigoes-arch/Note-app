from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class Register(serializers.Serializer):
    username=serializers.CharField(max_length=55)
    password=serializers.CharField(write_only=True)

    def validate_username(self,value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists")
        return value    

    def validate_password(self,value):
        users=User.objects.all()
        for user in users:
            if user.check_password(value):
                raise serializers.ValidationError("password exists")
        return value
        
    def create(self,validated_data):
        user=User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"]
        )   
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(
            username=data["username"],
            password=data["password"]
        )

        if not user:
            raise serializers.ValidationError("Invalid credentials")
        breakpoint()
        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)


        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }        