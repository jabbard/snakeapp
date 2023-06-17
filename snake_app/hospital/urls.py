from django.urls import path
from .views import HospitalViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'hospital', HospitalViewSet, basename='hospital')

urlpatterns = router.urls
