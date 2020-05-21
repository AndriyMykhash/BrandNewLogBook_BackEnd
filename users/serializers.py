# from django.contrib.auth.models import User, Group
from users.models import CustomUser
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'name', 'surname', 'email', 'type', 'learn_group', 'date_joined']


class SignUpUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'name', 'surname', 'type', 'date_joined']

