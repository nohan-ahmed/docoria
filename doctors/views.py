from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from core.permissions import IsOwnerOrReadOnly
# Local modules
from. import models
from. import serializers
# Create your views here.

class DoctorAPIView(ModelViewSet):
    queryset = models.Doctor.objects.all()
    serializer_class = serializers.DoctorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
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