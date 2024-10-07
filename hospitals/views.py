from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
# Local modules
from. import models
from. import serializers
from core.permissions import IsOwnerOrReadOnly
from .permissions import IsHospitalOwnerdOrReadOnly
# Create your views here.

class HospitalAPIView(ModelViewSet):
    queryset = models.Hospital.objects.all()
    serializer_class = serializers.HospitalSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ('id', 'user', 'name', 'contact_email', 'contact_number', 'opening_hours', 'specialties', 'created_at')
    search_fields = ('id', 'name', 'contact_email', 'contact_number', 'opening_hours','created_at')
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
class LocationAPIView(ModelViewSet):
    queryset = models.Location.objects.all()
    serializer_class = serializers.LocationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsHospitalOwnerdOrReadOnly ]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ('id', 'hospital', 'country', 'street_address', 'city', 'zip_code', 'created_at')
    search_fields = ('id', 'country', 'street_address', 'city', 'zip_code', 'created_at')
    
    
    def perform_create(self, serializer):
        serializer.save(hospital=self.request.user.hospitals.first())
        

class AddDoctorRequestAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly, IsHospitalOwnerdOrReadOnly]
    def post(self, request):
        try:
            # get the hospital from the authenticated user's hospital.
            from_hospital = self.request.user.hospitals.first()
            serializer = serializers.AddDoctorRequestSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(from_hospital=from_hospital)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
                
        except Exception as e:
            return Response({"error": "You don't have to permission to form this acction."}, status=status.HTTP_404_NOT_FOUND)
        
        