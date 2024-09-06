from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from volunteer.views import TaskViewSet, TimeLogViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'timelogs', TimeLogViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
