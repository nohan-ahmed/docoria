from rest_framework.viewsets import ModelViewSet
from. import models
from. import serializers
# Create your views here.

class HospitalAPIView(ModelViewSet):
    queryset = models.Hospital.objects.all()
    serializer_class = serializers.HospitalSerializer
    permission_classes = []
