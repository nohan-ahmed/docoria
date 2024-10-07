from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('doctors', views.DoctorAPIView)
router.register('specialization', views.SpecializationAPIView)

urlpatterns = [
    path('all-jobs/request/', views.ShowAllJobReauestAPIView.as_view()),
    path('respond-job/request/<int:id>/', views.RespondToJobRequestAPIView.as_view()),
    path('', include(router.urls))
]
