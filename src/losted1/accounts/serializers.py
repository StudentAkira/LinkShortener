from rest_framework import serializers

from accounts.models import CustomUser, ShortedLink


class CustomUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(min_length=4)
    password = serializers.CharField(min_length=4)

    class Meta:
        model = CustomUser
        fields = ['username', 'password']

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)


class UrlSerializer(serializers.ModelSerializer):
    long_url = serializers.URLField()
    short_url = serializers.URLField()


    class Meta:
        model = ShortedLink
        fields = ['long_url', 'short_url']

    def create(self, validated_data):
        return ShortedLink.objects.create(**validated_data)
