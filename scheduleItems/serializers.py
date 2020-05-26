from rest_framework import serializers

from learnGroups.models import LearnGroup
from lessons.models import Lesson
from scheduleItems.models import ScheduleItem


class ScheduleItemSerializer(serializers.HyperlinkedModelSerializer):
    group_id = serializers.SlugRelatedField(allow_null=True, slug_field="id", queryset=LearnGroup.objects.all())
    lesson_id = serializers.SlugRelatedField(allow_null=True, slug_field="id", queryset=Lesson.objects.all())

    class Meta:
        model = ScheduleItem
        # lesson = serializers.PrimaryKeyRelatedField(queryset=Lesson.objects.all(), write_only=True)
        # learn_group = serializers.PrimaryKeyRelatedField(queryset=LearnGroup.objects.all(), write_only=True)
        fields = ['id', 'group_id', 'lesson_id', 'start_at', 'end_at', 'day']
