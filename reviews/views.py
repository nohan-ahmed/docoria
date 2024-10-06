from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from. import models
from. import serializers
from .permissions import IsOwnerOrReadOnlyReview
# Create your views here.

class ReviewAPIView(ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnlyReview]
    def perform_create(self, serializer):
        serializer.save(patient=self.request.user.patient)