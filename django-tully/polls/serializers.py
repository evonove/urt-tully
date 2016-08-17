from rest_framework import serializers
from polls.models import Data
from django.contrib.auth.models import User

class PollSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Data


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
