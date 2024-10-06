from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from. import models
from. import serializers
from .permissions import IsOwnerOrReadOnlyReview
# Create your views here.

class ReviewAPIView(ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnlyReview]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ('id', 'patient', 'doctor', 'hospital', 'rating', 'created_at')
    search_fields = ('id', 'created_at')
    def perform_create(self, serializer):
        serializer.save(patient=self.request.user.patient)