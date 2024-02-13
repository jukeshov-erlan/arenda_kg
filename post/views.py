from rest_framework import generics
from .models import Auto, House, Category
from .serializers import *

class AutoApiView(generics.ListAPIView):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer

class HouseApiView(generics.ListAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer