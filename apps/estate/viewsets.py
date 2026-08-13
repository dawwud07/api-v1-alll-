from rest_framework.viewsets import ModelViewSet , ReadOnlyModelViewSet

from .models import Appartment , Object , Block
from .serializers import AppartmentSerializer , ObjectSerializer , BlockSerializer
from api.plaginations import SimplePagination
from rest_framework.permissions import IsAdminUser , AllowAny 
from rest_framework import permissions
from api.permissions import IsSuperUser
from rest_framework.filters import SearchFilter , OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class AppartmentViewSet(ModelViewSet):
    serializer_class = AppartmentSerializer
    queryset = Appartment.objects.all()
    pagination_class = SimplePagination
    permission_classes = [AllowAny]
    filter_backends = (DjangoFilterBackend , SearchFilter , OrderingFilter)
    filterset_fields = ["rooms_count" , "type", "block"]
    ordering_fields = ["number" , "floor"]
    search_fields = ["block__object_name",  ]
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update']:
            return [permissions.IsAdminUser()]
        elif self.action == "delete" :
            return [IsSuperUser()]
        return super().get_permissions()
    
    
    # def get_queryset(self):
    #     qs = Appartment.objects.all()
    #     block_number = self.request.query_params.get("block_number")
    #     print(block_number)
    #     qs  = qs.filter(block_number = block_number)
    #     return qs
        


class ObjectViewSet(ModelViewSet):
    serializer_class = ObjectSerializer
    queryset = Object.objects.all()
    pagination_class = SimplePagination
    permission_classes = [AllowAny]
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update']:
                return [permissions.IsAdminUser()]
        elif self.action == "delete" :
                return [IsSuperUser()]
        return super().get_permissions()

    
class BlockViewSet(ModelViewSet):
    serializer_class = BlockSerializer
    queryset = Block.objects.all()
    pagination_class = SimplePagination
    permission_classes =[AllowAny]
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update']:
                    return [permissions.IsAdminUser()]
        elif self.action == "delete" :
                    return [IsSuperUser()]
        return super().get_permissions()
    
    
    























