from rest_framework import serializers
from .models import *

class AutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auto
        fields = '__all__'


class HouseSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = House
        fields = ('name', 'location', 'price', 'price_currency', 'user')