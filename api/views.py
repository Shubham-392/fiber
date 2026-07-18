from rest_framework import viewsets, permissions
from rest_framework.generics import ListAPIView
from .models import User, Transportation
from .serializers import UserHyperLinkSerializer, TransportationSerializer


class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserHyperLinkSerializer
    permission_classes = [permissions.IsAuthenticated]

class TransferGenericAPIView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TransportationSerializer

    def get_queryset(self):
        user = self.request.user
        return Transportation.objects.filter(sender=user)