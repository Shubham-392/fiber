from .models import User
from rest_framework.serializers import HyperlinkedModelSerializer

class UserHyperLinkSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'password']