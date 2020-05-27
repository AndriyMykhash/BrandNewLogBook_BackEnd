from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
import datetime

# Create your models here.


class LearnGroup(models.Model):
    id = models.CharField(max_length=5, primary_key=True)
    course = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)], null=False)
    start_on = models.DateField(null=False, default=datetime.date.today)
    ends_on = models.DateField(null=False, default=datetime.date.today)

    def __str__(self):
        return self.id
