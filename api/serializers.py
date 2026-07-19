from .models import Transportation
from rest_framework import serializers



class TransportationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transportation
        fields = ['sender', 'receiver', 'human_readable_size']

class RecordTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transportation
        fields = ['receiver', 'file']

class RecordTransferResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transportation
        fields = '__all__'