from rest_framework import serializers

from FieldValue.models import Field, FieldValue


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = ['id', 'name', 'alias', 'fieldvalue_set']


class FieldValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldValue
        fields = ['id', 'field', 'value', 'item']
