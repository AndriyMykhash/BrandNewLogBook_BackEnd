from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions

# Create your views here.
from lessons.models import Lesson
from lessons.serializers import LessonSerializer


class LesonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all().order_by('-start_on')
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]