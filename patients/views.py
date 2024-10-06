from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
# local modules
from . import models
from . import serializers
from core.permissions import IsOwnerOrReadOnly
# Create your views here.


class PatientAPIView(ModelViewSet):
    queryset = models.Patient.objects.all()
    serializer_class = serializers.PatientSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ('id', 'user', 'contact_number', 'insurance_provider', 'insurance_number', 'created_at')
    search_fields = ('id', 'contact_number', 'blood_type', 'insurance_provider', 'insurance_number', 'created_at')
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)