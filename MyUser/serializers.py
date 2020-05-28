from rest_framework import serializers
from MyUser.models import TmcUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TmcUser
        fields = ['id', 'username', 'password', 'email', 'is_superuser']
