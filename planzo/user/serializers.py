from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

MyUser = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ["id", "email", "date_of_birth", "is_active", "is_admin"]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = MyUser
        fields = ["email", "date_of_birth", "password"]

    def create(self, validated_data):
        user = MyUser.objects.create_user(
            email=validated_data["email"],
            date_of_birth=validated_data["date_of_birth"],
            password=validated_data["password"],
        )
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(email=data["email"], password=data["password"])
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        return {"user": user}


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ["email", "date_of_birth"]
