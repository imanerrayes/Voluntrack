from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, TimeLogViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'timelogs', TimeLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
