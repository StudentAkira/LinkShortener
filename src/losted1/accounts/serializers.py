from rest_framework import serializers

from accounts.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(min_length=4)
    password = serializers.CharField(min_length=4)

    class Meta:
        model = CustomUser
        fields = ['username', 'password']

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)

