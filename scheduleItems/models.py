from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.timezone import utc, now

# Create your models here.
from learnGroups.models import LearnGroup
from lessons.models import Lesson


class ScheduleItem(models.Model):
    id = models.AutoField(primary_key=True)
    group_id = models.ForeignKey(LearnGroup, on_delete=models.CASCADE, related_name="learnGroup")
    lesson_id = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="lesson")
    duration = models.TimeField(default=now, null=False)

    def __str__(self):
        return self.id
