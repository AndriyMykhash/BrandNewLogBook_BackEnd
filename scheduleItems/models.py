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
    start_at = models.TimeField(default=now, null=False)
    end_at = models.TimeField(default=now, null=False)

    DAYS = [("MONDAY", "Monday"), ("TUESDAY", "Tuesday"), ("WEDNESDAY", "Wednesday"), ("THURSDAY", "Thursday"),
            ("FRIDAY", "Friday"), ("SATURDAY", "Saturday"), ("SUNDAY", "Sunday")]
    day = models.CharField(choices=DAYS, max_length=10, default="MONDAY", null=False)

    def __str__(self):
        return str(self.group_id)
