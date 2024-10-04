from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from. import models
from. import serializers
from core.permissions import IsOwnerOrReadOnly
# Create your views here.

class EducationAPIView(ModelViewSet):
    queryset = models.Education.objects.all()
    serializer_class = serializers.EducationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)