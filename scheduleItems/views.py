from rest_framework import viewsets, serializers, permissions

from scheduleItems.models import ScheduleItem
from scheduleItems.serializers import ScheduleItemSerializer


class ScheduleItemViewSet(viewsets.ModelViewSet):
    queryset = ScheduleItem.objects.all().order_by('-id')
    serializer_class = ScheduleItemSerializer
    permission_classes = [permissions.IsAuthenticated]
