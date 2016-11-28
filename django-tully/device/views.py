from django.shortcuts import redirect
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework import generics, permissions, response, renderers, viewsets
from rest_framework.authentication import BasicAuthentication

from device.models import Data
from device.serializers import DataSerializer


class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all().order_by('-created')
    serializer_class = DataSerializer
    permission_classes = (permissions.IsAuthenticated, )


class DataViews(LoginRequiredMixin, ListView):
    model = Data
    queryset = Data.objects.all()
    template_name = 'device/datas_list.html'
