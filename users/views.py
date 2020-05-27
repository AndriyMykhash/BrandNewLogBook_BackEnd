from abc import ABC

import django_filters
import jwt
from django.contrib.auth import user_logged_in
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_jwt.serializers import jwt_payload_handler
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import filters
from django_filters.rest_framework.backends import DjangoFilterBackend

from brand_new_logbook_be import settings
from users.models import CustomUser
from rest_framework import viewsets, status
from rest_framework import permissions
from users.serializers import UserSerializer, SignUpUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [f.name for f in CustomUser._meta.get_fields()]
    permission_classes = [permissions.IsAuthenticated]


class TokenObtainPairWithIdSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super(TokenObtainPairWithIdSerializer, self).validate(attrs)
        data.update({'userId': self.user.id})
        data.update({'group': self.user.learn_group.id})

        return data


class TokenObtainPairViewWithId(TokenObtainPairView):
    serializer_class = TokenObtainPairWithIdSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def create_auth(request):
    serialized = SignUpUserSerializer(data=request.POST)
    if serialized.is_valid():
        CustomUser.objects.create_user(email=serialized.data["email"],
                                       password=serialized.data["password"],
                                       name=serialized.data["name"],
                                       surname=serialized.data["surname"],
                                       type=serialized.data["type"])
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)
