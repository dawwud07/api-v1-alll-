from rest_framework import serializers

from .models import Appartment , Object , Block


class AppartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appartment
        fields = "__all__"
      
        
class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = "__all__"
    
        
class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = "__all__"
            

class AppartmentSerializer(serializers.Serializer):
    number = serializers.IntegerField()
    area = serializers.FloatField()
    floor = serializers.IntegerField()
    rooms_count = serializers.IntegerField()
    deadline = serializers.DateField()
    type = serializers.ChoiceField(choices=Appartment.TYPE_CHOICES)
    block = serializers.PrimaryKeyRelatedField(queryset=Block.objects.all())

    def create(self, validated_data):
        return Appartment.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.number = validated_data.get('number',instance.number)
        instance.area = validated_data.get('area',instance.area)
        instance.floor = validated_data.get('floor',instance.floor)
        instance.rooms_count = validated_data.get('rooms_count',instance.rooms_count)
        instance.deadline = validated_data.get('deadline',instance.deadline)
        instance.type = validated_data.get('type',instance.type)
        instance.block = validated_data.get('block',instance.block)
        instance.save()
