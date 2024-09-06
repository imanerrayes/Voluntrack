from django.db import models
from django.contrib.auth.models import User
from geopy.distance import geodesic

class VolunteerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_hours = models.FloatField(default=0.0)
    location = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    assigned_to = models.ForeignKey(VolunteerProfile, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='Pending')
    location_lat = models.FloatField()
    location_lon = models.FloatField()

    def __str__(self):
        return self.title

class TimeLog(models.Model):
    volunteer = models.ForeignKey(VolunteerProfile, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    clock_in_lat = models.FloatField()
    clock_in_lon = models.FloatField()

    def duration(self):
        if self.end_time and self.start_time:
            return (self.end_time - self.start_time).total_seconds() / 3600
        return 0

    def is_in_geofence(self):
        task_location = (self.task.location_lat, self.task.location_lon)
        volunteer_location = (self.clock_in_lat, self.clock_in_lon)
        distance = geodesic(task_location, volunteer_location).meters
        return distance <= 200  # 200 meters geofence
