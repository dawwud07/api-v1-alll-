from rest_framework.generics import (
    ListAPIView , CreateAPIView , RetrieveAPIView , 
    UpdateAPIView , DestroyAPIView , 
    ListCreateAPIView , RetrieveUpdateDestroyAPIView ,
    RetrieveUpdateAPIView , RetrieveDestroyAPIView
)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models  import Appartment , Object , Block 
from .serializers import AppartmentSerializer


# class ApartmentListAPIView(ListAPIView):
#     serializer_class = AppartmentSerializer
#     queryset = Appartment.objects.all()
    
    
# class ApartmentCreateAPIView(CreateAPIView):
#     serializer_class = AppartmentSerializer
#     queryset = Appartment.objects.all()
    
    
# class ApartmentRetrieveAPIView(RetrieveAPIView):
#     serializer_class = AppartmentSerializer
#     queryset = Appartment.objects.all()


# class ApartmentUpdateAPIView(UpdateAPIView):
#     serializer_class = AppartmentSerializer
#     queryset = Appartment.objects.all()


# class ApartmentDestroyAPIView(DestroyAPIView):
#     serializer_class = AppartmentSerializer
#     queryset = Appartment.objects.all()

class ApartmentListCreateAPIView(ListCreateAPIView):
    serializer_class = AppartmentSerializer
    queryset = Appartment.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ["rooms_count", "type", "block"]
    ordering_fields = ["number", "floor"]
    search_fields = ["block__object_name"]
    
    
class ApartmentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = AppartmentSerializer
    queryset = Appartment.objects.all()
    
    
    
