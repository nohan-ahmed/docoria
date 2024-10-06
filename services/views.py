from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from . import models
from . import serializers
from .permissions import IsOwnerOrReadOnlyService
# Create your views here.
class ServiceAPIView(ModelViewSet):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer
    permission_classes = [IsOwnerOrReadOnlyService]
    
    def perform_create(self, serializer):
        serializer.save(hospital=self.request.user.hospitals.all().first())

