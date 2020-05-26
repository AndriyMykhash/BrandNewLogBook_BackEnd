from rest_framework import serializers

from learnGroups.models import LearnGroup


class LearnGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LearnGroup
        fields = ['id', 'course', 'start_on', 'ends_on']
