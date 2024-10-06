from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('users', views.UserAPIView)
router.register('address', views.AddressAPIView)

urlpatterns = [
    path("register/", views.RegisterAPIView.as_view()),
    path("verify-email/<uid>/<token>/", views.VerifyEmailAPIView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('password-change/', views.PasswordChangeAPIView.as_view()),
    path('password-reset/request/', views.PasswordResetRequestAPIView.as_view()),
    path('password-reset/<uid>/<token>/', views.PasswordResetAPIView.as_view()),
    path('logout/', views.UserLogoutAPIView.as_view()),
    path('', include(router.urls))
]
