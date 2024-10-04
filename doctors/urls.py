from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('doctors', views.DoctorAPIView)

urlpatterns = [
    path('', include(router.urls))
]
