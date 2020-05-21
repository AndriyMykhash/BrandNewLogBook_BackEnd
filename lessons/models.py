from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.timezone import utc, now

# Create your models here.


class Lesson(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    credit_price = models.IntegerField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
