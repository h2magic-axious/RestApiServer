from rest_framework import serializers
from MyUser.models import TmcUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TmcUser
        fields = ['id', 'username', 'password', 'email', 'phone_number', 'is_superuser']

    def create(self, validated_data):
        user = TmcUser(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
