from rest_framework import viewsets
from rest_framework.response import Response
from django.utils import timezone
from .models import VolunteerProfile, Task, TimeLog
from .serializers import VolunteerProfileSerializer, TaskSerializer, TimeLogSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TimeLogViewSet(viewsets.ModelViewSet):
    queryset = TimeLog.objects.all()
    serializer_class = TimeLogSerializer

    def perform_create(self, serializer):
        task = serializer.validated_data['task']
        clock_in_lat = serializer.validated_data['clock_in_lat']
        clock_in_lon = serializer.validated_data['clock_in_lon']

        # Check if volunteer is in the geofence
        timelog = TimeLog(task=task, clock_in_lat=clock_in_lat, clock_in_lon=clock_in_lon)
        if not timelog.is_in_geofence():
            return Response({"error": "Volunteer is not within the geofenced area."}, status=400)

        timelog.start_time = timezone.now()
        timelog.save()

    def update(self, request, *args, **kwargs):
        timelog = self.get_object()
        timelog.end_time = timezone.now()
        timelog.save()

        # Update volunteer's total hours
        volunteer = timelog.volunteer
        volunteer.total_hours += timelog.duration()
        volunteer.save()

        return Response(self.get_serializer(timelog).data)
