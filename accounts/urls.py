from django.urls import path, include
from . import views

urlpatterns = [
    path("register/", views.RegisterAPIView.as_view()),
    path("verify-email/<uid>/<token>/", views.VerifyEmailAPIView.as_view()),
]
