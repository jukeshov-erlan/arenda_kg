from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from rest_framework.authentication import TokenAuthentication
from .serializers import *

class AutoViewSet(viewsets.ModelViewSet):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        categories = Category.objects.get(pk=pk)
        return Response({'categories': categories.name})





class HouseAPIList(generics.ListCreateAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class HouseAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication)

class HouseAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    permission_classes = (IsAdminOrReadOnly, )



# class HouseViewSet(viewsets.ModelViewSet):
#     # queryset = House.objects.all()
#     serializer_class = HouseSerializer

#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#         if not pk:
#             return House.objects.all()[:3]
#         return House.objects.filter(pk=pk)




