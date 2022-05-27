from rest_framework import serializers


class ApplicationSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField(max_length=200)
    phone_number = serializers.CharField(max_length=200)
    business_type = serializers.CharField(max_length=200)