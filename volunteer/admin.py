from django.contrib import admin
from .models import VolunteerProfile, Task, TimeLog

admin.site.register(VolunteerProfile)
admin.site.register(Task)
admin.site.register(TimeLog)
