from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework import permissions
import logging
from rest_framework.permissions import BasePermission
# Create your views here.
from lessons.models import Lesson
from lessons.serializers import LessonSerializer
from rest_framework.authtoken.models import Token
from users.models import CustomUser

logger = logging.getLogger(__name__)


class TeacherPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        type = CustomUser.objects.get(id=user.id).type
        return type == "ADM" or type == "TCH"


class LesonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all().order_by('-id')
    serializer_class = LessonSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [f.name for f in Lesson._meta.get_fields()]
    permission_classes = [permissions.IsAuthenticated & TeacherPermission]
