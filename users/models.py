from enum import Enum

from django.contrib.auth.models import AbstractUser
from django.db import models

from rest_framework.authtoken.models import Token

# Create your models here.
from learnGroups.models import LearnGroup
from users.managers import CustomUserManager
from django.utils.timezone import utc, now


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)
    name = models.CharField(max_length=20, default="Anonymous", null=False)
    surname = models.CharField(max_length=40, default="Anonymous", null=False)
    TYPES = (("ADM", "Admin"), ("STD", "Student"), ("TCH", "Teacher"))
    type = models.CharField(choices=TYPES, max_length=50, default="STD")
    date_joined = models.DateField(null=False, auto_now=True, auto_created=True)
    learn_group = models.ForeignKey(LearnGroup, on_delete=models.CASCADE, related_name="StudLearnGroup",
                                    null=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def token(self):
        return Token.objects.create(user=self)

    def __str__(self):
        return self.email
