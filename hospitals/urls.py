from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('hospitals', views.HospitalAPIView)
router.register('location', views.LocationAPIView)
urlpatterns = [
    path('add-doctor/request/', views.AddDoctorRequestAPIView.as_view()),
    path('', include(router.urls))
]
