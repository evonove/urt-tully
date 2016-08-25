from rest_framework import serializers
from device.models import Data
from django.contrib.auth.models import User

class DataSerializer(serializers.ModelSerializer):

    class Meta:
        model = Data


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
