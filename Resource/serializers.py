from rest_framework import serializers
from Resource.models import ResourceType, ResourceContent


class ResourceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceType
        fields = ['id', 'name', 'alias', 'resourcecontent_set']


class ResourceContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceContent
        fields = '__all__'
