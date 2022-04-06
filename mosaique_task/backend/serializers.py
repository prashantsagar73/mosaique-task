from rest_framework import serializers
from .models import *


class weatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ['temprature','wather_name','time_stamp','images']