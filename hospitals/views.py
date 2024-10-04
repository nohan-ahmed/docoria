from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from. import models
from. import serializers
from core.permissions import IsOwnerOrReadOnly
from .permissions import IsHospitalOwnerdOrReadOnly
# Create your views here.

class HospitalAPIView(ModelViewSet):
    queryset = models.Hospital.objects.all()
    serializer_class = serializers.HospitalSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
class LocationAPIView(ModelViewSet):
    queryset = models.Location.objects.all()
    serializer_class = serializers.LocationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsHospitalOwnerdOrReadOnly ]
    
    def perform_create(self, serializer):
        serializer.save(hospital=self.request.user.hospitals.first())