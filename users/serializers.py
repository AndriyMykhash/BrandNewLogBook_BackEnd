# from django.contrib.auth.models import User, Group
from learnGroups.models import LearnGroup
from users.models import CustomUser
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    learn_group = serializers.SlugRelatedField(allow_null=True, slug_field="id", queryset=LearnGroup.objects.all())

    class Meta:
        model = CustomUser
        fields = ['id', 'name', 'surname', 'email', 'learn_group', 'type', 'date_joined']


class SignUpUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'name', 'surname', 'type', 'date_joined']
