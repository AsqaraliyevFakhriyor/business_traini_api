from rest_framework import serializers

from .models import ApplicationModel as Apps


class ApplicationSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    username = serializers.CharField(max_length=200)
    email = serializers.EmailField(max_length=200)
    phone_number = serializers.CharField(max_length=200)
    business_type = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return Apps.objects.create(**validated_data)
