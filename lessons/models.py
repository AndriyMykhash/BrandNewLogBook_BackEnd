from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.timezone import utc, now

# Create your models here.


class Lesson(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    course = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    created_on = models.DateTimeField(auto_now_add=True)
    start_on = models.DateField(null=False, default=now)
    ends_on = models.DateField(null=False, default=now)

    def __str__(self):
        return self.title
