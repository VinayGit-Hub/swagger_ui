from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StreamViewSet

router = DefaultRouter()
router.register('streams', StreamViewSet)

urlpatterns = [
    path('', include(router.urls)),
]