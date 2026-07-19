from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .models import  Transportation
from .serializers import  TransportationSerializer, RecordTransferSerializer, RecordTransferResponseSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from drf_spectacular.utils import extend_schema, OpenApiResponse
from django.utils import timezone
from .utils import sizeof_fmt


class RecordTransferAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RecordTransferResponseSerializer
    parser_classes = [MultiPartParser, FormParser]

    @extend_schema(
            request={
                'multipart/form-data': RecordTransferSerializer,
            },
            responses={201: OpenApiResponse(
                        response=RecordTransferResponseSerializer,
                        description='File transferred successfully.'
                    )}
        )
    def post(self, request):
        """
        API View to give the user ability to send files to another user
        """
        # validate the data in serializer first
        serializer = RecordTransferSerializer(data=request.data)
        
        if serializer.is_valid():
            # check if the authenticated user is the original sender
            # if not, return a 403 Forbidden response
            
            # calculate the size of the file
            # as size is not in the post request, we need to calculate it here
            file_size_in_bytes = serializer.validated_data['file'].size
            serializer.validated_data['human_readable_size'] = sizeof_fmt(file_size_in_bytes)
            
            receiver = serializer.validated_data['receiver']
            
            # create a db entry for this transcation
            serialise_instance = serializer.save(
                sender=request.user, 
                receiver=receiver, 
                file_size=file_size_in_bytes,
                file=serializer.validated_data['file'], 
                sent_at=timezone.now()
            )
            response_data = RecordTransferResponseSerializer(serialise_instance).data
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "error": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)


class TransferGenericAPIView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TransportationSerializer

    def get_queryset(self):
        user = self.request.user
        return Transportation.objects.filter(sender=user)
