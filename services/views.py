from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

# Local modules
from . import models
from . import serializers
from .permissions import IsOwnerOrReadOnlyService
# Create your views here.
class ServiceAPIView(ModelViewSet):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnlyService]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ('id','hospital','name', 'price', 'duration', 'is_available','specialization', 'created_at')
    search_fields =  ('id', 'name', 'is_available', 'created_at')
    
    def perform_create(self, serializer):
        serializer.save(hospital=self.request.user.hospitals.all().first())

