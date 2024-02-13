from rest_framework import serializers
from .models import *
from .serializers import *

class AutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auto
        fields = '__all__'


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'
