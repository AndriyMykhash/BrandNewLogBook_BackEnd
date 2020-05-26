from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, serializers, permissions

from scheduleItems.models import ScheduleItem
from scheduleItems.serializers import ScheduleItemSerializer


class ScheduleItemViewSet(viewsets.ModelViewSet):
    queryset = ScheduleItem.objects.all().order_by('-id')
    serializer_class = ScheduleItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [f.name for f in ScheduleItem._meta.get_fields()]
    permission_classes = [permissions.IsAuthenticated]
