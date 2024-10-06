from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from. import models
from. import serializers
from core.permissions import IsOwnerOrReadOnly
# Create your views here.

class EducationAPIView(ModelViewSet):
    queryset = models.Education.objects.all()
    serializer_class = serializers.EducationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ('id', 'user', 'country', 'institution', 'degree', 'field_of_study', 'start_date', 'end_date', 'gpa', 'created_at')
    search_fields = ('id', 'institution', 'degree', 'field_of_study', 'start_date', 'end_date', 'gpa', 'created_at')
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)