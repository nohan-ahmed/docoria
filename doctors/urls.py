from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('doctors', views.DoctorAPIView)
router.register('specialization', views.SpecializationAPIView)

urlpatterns = [
    path('', include(router.urls))
]
