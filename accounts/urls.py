from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

urlpatterns = [
    path("register/", views.RegisterAPIView.as_view()),
    path("verify-email/<uid>/<token>/", views.VerifyEmailAPIView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('password-change/', views.PasswordChangeAPIView.as_view()),
]
