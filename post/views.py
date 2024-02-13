from rest_framework import generics, viewsets
from .serializers import *

class AutoViewSet(viewsets.ModelViewSet):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer




# class AutoApiList(generics.ListCreateAPIView):
#     queryset = Auto.objects.all()
#     serializer_class = AutoSerializer

class HouseApiView(generics.ListAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer