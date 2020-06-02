from MyUser.serializers import UserSerializer
from MyUser.models import TmcUser
from rest_framework import generics
from rest_framework_jwt.utils import jwt_decode_handler
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated

def get_user(request):
    token = request.GET.get('token', None)
    if token:
        token_user = jwt_decode_handler(token)
        return JsonResponse({
            'username': token_user['username']
        })
    else:
        return JsonResponse({
            'username': None
        })


class UserList(generics.ListCreateAPIView):
    queryset = TmcUser.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TmcUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]