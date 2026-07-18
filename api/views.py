from rest_framework import viewsets, permissions
from .models import User
from .serializers import UserHyperLinkSerializer


class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserHyperLinkSerializer
    permission_classes = [permissions.IsAuthenticated]