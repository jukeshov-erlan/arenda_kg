from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import *

class AutoViewSet(viewsets.ModelViewSet):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer

class HouseViewSet(viewsets.ModelViewSet):
    # queryset = House.objects.all()
    serializer_class = HouseSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return House.objects.all()[:3]
        return House.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        categories = Category.objects.get(pk=pk)
        return Response({'categories': categories.name})



