from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from. import models
from. import serializers
# Create your views here.
class AppointmentAPIView(ModelViewSet):
    queryset = models.Appointment.objects.all()
    serializer_class = serializers.AppointmentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ('id', 'doctor', 'patient', 'hospital', 'appointment_type','status', 'created_at')
    search_fields = ('id', 'appointment_type', 'status', 'created_at')
    def perform_create(self, serializer):
        serializer.save(patient=self.request.user.patient)