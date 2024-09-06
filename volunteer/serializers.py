from rest_framework import serializers
from .models import VolunteerProfile, Task, TimeLog

class VolunteerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteerProfile
        fields = ['user', 'total_hours', 'location']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'assigned_to', 'status', 'location_lat', 'location_lon']

class TimeLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeLog
        fields = ['volunteer', 'task', 'start_time', 'end_time', 'clock_in_lat', 'clock_in_lon', 'is_in_geofence', 'duration']
