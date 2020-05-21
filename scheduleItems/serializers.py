from rest_framework import serializers
from scheduleItems.models import ScheduleItem


class ScheduleItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ScheduleItem
        # lesson = serializers.PrimaryKeyRelatedField(queryset=Lesson.objects.all(), write_only=True)
        # learn_group = serializers.PrimaryKeyRelatedField(queryset=LearnGroup.objects.all(), write_only=True)
        fields = ['group_id', 'lesson_id', 'duration']
