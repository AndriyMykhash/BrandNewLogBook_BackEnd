from rest_framework import serializers

from lessons.models import Lesson
from users.models import CustomUser


class LessonSerializer(serializers.HyperlinkedModelSerializer):
    # teacher = serializers.SlugRelatedField(allow_null=True, slug_field="id", queryset=CustomUser.objects.get(type="TCH"))
    teacher_id = serializers.PrimaryKeyRelatedField(allow_null=True,
                                                 queryset=CustomUser.objects.all().filter(type__in=["ADM", "TCH"]))
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'description', 'credit_price', 'teacher_id']
