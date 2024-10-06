from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

# Local modules
from . import models
from . import serializers
from core.permissions import IsOwnerOrReadOnly

# Create your views here.
class StaffAPIView(ModelViewSet):
    queryset = models.Staff.objects.all()
    serializer_class = serializers.StaffSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ('id', 'user','job_title', 'created_at')
    search_fields = ('id', 'job_title', 'created_at')
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)