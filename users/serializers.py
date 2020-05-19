# from django.contrib.auth.models import User, Group
from users.models import CustomUser
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'name', 'surname', 'email', 'type', 'date_joined']


class SignUpUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'name', 'surname', 'type', 'date_joined']

