from rest_framework import serializers
from device.models import Data

class DataSerializer(serializers.ModelSerializer):

    class Meta:
        model = Data
