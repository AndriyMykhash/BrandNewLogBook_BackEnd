from django.shortcuts import render


# Create your views here.
from rest_framework import viewsets, permissions

from learnGroups.models import LearnGroup
from learnGroups.serializers import LearnGroupSerializer


class LearnGroupViewSet(viewsets.ModelViewSet):
    queryset = LearnGroup.objects.all().order_by('-start_on')
    serializer_class = LearnGroupSerializer
    permission_classes = [permissions.IsAuthenticated]
