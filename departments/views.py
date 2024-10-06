from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from core.permissions import IsOwnerOrReadOnly
# Local modules
from. import models
from. import serializers
# Create your views here.

class DepartmentAPIView(ModelViewSet):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ('id', 'name', 'hospital', 'doctors', 'staffs', 'services', 'created_at')

    search_fields = ('id', 'name', 'created_at')
    
    def perform_create(self, serializer):
        """
        perform_create Method: This method is a hook provided by Django REST Framework's ModelViewSet. 
        It allows you to customize the creation of a model instance without completely overriding the create method.
        """
        
        """
        Setting the author: By calling serializer.save(author=self.request.user), you automatically set the author field to the currently authenticated user when a post is created.
        This ensures that the author is set correctly and prevents users from tampering with the field
        """
        serializer.save(hospital=self.request.user.hospitals.first())
        
