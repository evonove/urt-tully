from device.models import Data
from device.serializers import DataSerializer
from rest_framework import generics, permissions, response, renderers, viewsets
from device.permissions import IsOwnerOrReadOnly

class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
