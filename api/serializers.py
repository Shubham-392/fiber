from .models import User, Transportation
from rest_framework import serializers

class UserHyperLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'password']

class TransportationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transportation
        fields = ['sender', 'receiver', 'size']