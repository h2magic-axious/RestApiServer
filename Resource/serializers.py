from rest_framework import serializers
from Resource.models import ResourceType, ResourceContent


class ResourceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceType
        fields = '__all__'


class ResourceContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceContent
        fields = '__all__'
