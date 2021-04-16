from decouple import config
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from api.serializers import RegisterUserSerializer, listUserSerializer

# Create your views here.

class get_token(ObtainAuthToken):
    "This will generate the token"
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, 
                            context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, create = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        }, status=200)

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_class = (AllowAny,)
    serializer_class = RegisterUserSerializer

class get_all_Users(APIView):
    permission_class = (IsAuthenticated, )
    def get(self, request):
        users = User.objects.all()
        serializer = listUserSerializer(users, many=True)
        return Response(serializer.data)

