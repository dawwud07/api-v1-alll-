from django.shortcuts import render 

from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated , AllowAny ,IsAdminUser , IsAuthenticatedOrReadOnly
from rest_framework import status
from rest_framework.decorators import permission_classes
from .models import Appartment , Object , Block
from .serializers import AppartmentSerializer , ObjectSerializer , BlockSerializer 







@api_view(['GET'])
@permission_classes([AllowAny])
def apartments_list(request):
    appartments = Appartment.objects.all()
    serializer = AppartmentSerializer(appartments , many = True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def apartments_post(request):
    serializer = AppartmentSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors)




@api_view(['GET'])
@permission_classes([AllowAny])
def objects_list(request):
    objects = Object.objects.all()
    serializer = ObjectSerializer(objects , many = True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def objects_post(request):
    serializer = ObjectSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
    
    
@api_view(['PUT'])
@permission_classes([IsAdminUser])
def appartment_put(requst , pk):
    appartment = Appartment.objects.get(pk=pk)
    seriliazer = AppartmentSerializer( data=requst.data , instance=appartment) 
    if seriliazer.is_valid():
        seriliazer.save()
        return Response(seriliazer.data ,)
    return Response(seriliazer.errors)    


@api_view(['GET'])
@permission_classes([AllowAny])
def blocks_list(request):
    blocks = Block.objects.all()
    serializer = BlockSerializer(blocks , many = True)
    return Response(serializer.data)
    
    
@api_view(['POST'])
@permission_classes([IsAdminUser])
def blocks_post(request):
    serializer = BlockSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors)


@api_view(['GET'])
@permission_classes([AllowAny])
def blocks_list(request):
    blocks = Block.objects.all()
    serializer = BlockSerializer(blocks , many = True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def appartment_detail(request , pk):
    appartment = Appartment.objects.get(pk=pk)
    serializer = AppartmentSerializer(appartment)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def appartment_delete(request , pk ):
    appartment = Appartment.objects.get(pk=pk)
    appartment.delete()
    return Response({ 'message': 'DELETED'})

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def object_delete(request , pk ) :
    objects = Object.objects.get(pk = pk)
    objects.delete()
    return Response({'message' : 'delete'})

@api_view(['GET'])
@permission_classes([AllowAny])
def object_detail(request , pk) : 
    objects = Object.objects.get(pk = pk )
    serealizer = ObjectSerializer(objects)
    return Response(serealizer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def block_detail(request , pk) : 
    blocks = Block.objects.get(pk = pk )
    serealizer = BlockSerializer(blocks)
    return Response(serealizer.data)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def block_delete(request , pk ) :
    blocks = Block.objects.get(pk = pk)
    blocks.delete()
    return Response({'message' : 'delete'})



@api_view(['PUT'])
@permission_classes([IsAdminUser])
def block_put(request , pk):
    blocks = Block.objects.get(pk=pk)
    serializer = BlockSerializer(data=request.data , instance=blocks)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors)



@api_view(['PUT'])
@permission_classes([IsAdminUser])
def object_put(request , pk):
    objects = Object.objects.get(pk=pk)
    serializer = ObjectSerializer(data=request.data , instance=objects)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors)




