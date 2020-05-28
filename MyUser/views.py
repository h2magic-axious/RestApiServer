from MyUser.serializers import UserSerializer
from MyUser.models import TmcUser
from rest_framework import generics


class UserList(generics.ListCreateAPIView):
    queryset = TmcUser.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TmcUser.objects.all()
    serializer_class = UserSerializer
