# from django.contrib.auth.models import User, Group
from users.models import CustomUser
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'type', 'date_joined']
