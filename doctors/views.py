from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from core.permissions import IsOwnerOrReadOnly
# Local modules
from. import models
from. import serializers
from hospitals.models import AddDoctorRequest, Hospital
from hospitals.serializers import AddDoctorRequestSerializer
# Create your views here.

class DoctorAPIView(ModelViewSet):
    queryset = models.Doctor.objects.all()
    serializer_class = serializers.DoctorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ('id', 'user', 'specialization', 'experience', 'created_at')
    search_fields = ('id', 'experience', 'created_at')
    
    def perform_create(self, serializer):
        """
        perform_create Method: This method is a hook provided by Django REST Framework's ModelViewSet. 
        It allows you to customize the creation of a model instance without completely overriding the create method.
        """
        
        """
        Setting the author: By calling serializer.save(author=self.request.user), you automatically set the author field to the currently authenticated user when a post is created.
        This ensures that the author is set correctly and prevents users from tampering with the field
        """
        serializer.save(user=self.request.user)
        

class SpecializationAPIView(ModelViewSet):
    queryset = models.Specialization.objects.all()
    serializer_class = serializers.SpecializationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ('id', 'name', 'slug', 'created_at')
    search_fields = ('id', 'name', 'slug', 'created_at')
    
class ShowAllJobReauestAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        try:
            doctor = request.user.doctor 
            queryset = AddDoctorRequest.objects.filter(to_doctor=doctor, status='pending')
            serializer = AddDoctorRequestSerializer(queryset, many=True)
            return Response(serializer.data)
        except Exception:
            return Response({'error':'This feature is only available on the doctor account.'})

# Accept/Reject a Job Request
class RespondToJobRequestAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, id, format=None):
        try:
            doctor = request.user.doctor  # Get the authenticated doctor
            add_doctor_request = AddDoctorRequest.objects.get(pk=id, to_doctor=doctor)
        except models.Doctor.DoesNotExist:
            return Response({'error': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)
        
        except AddDoctorRequest.DoesNotExist:
            return Response({'error': 'Job request not found'}, status=status.HTTP_404_NOT_FOUND)
        
        status_choice = request.data.get('status', '').lower()
        if status_choice == 'accepted':
            add_doctor_request.status = 'accepted'

            add_doctor_request.from_hospital.doctors.add(add_doctor_request.to_doctor)
            add_doctor_request.from_hospital.save()
        
        elif status_choice == 'rejected':
            add_doctor_request.status = 'rejected'
        else:
            return Response({"status": ["Invalid status"]}, status=status.HTTP_400_BAD_REQUEST)
        
        add_doctor_request.save() # Save the add_doctor_request obj
        return Response({'status': add_doctor_request.status}, status=status.HTTP_200_OK)
