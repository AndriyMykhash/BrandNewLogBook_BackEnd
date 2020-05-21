from django.shortcuts import render

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
    queryset = Lesson.objects.all().order_by('-start_on')
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated & TeacherPermission]
