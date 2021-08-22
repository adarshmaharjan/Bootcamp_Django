from decimal import Context
from django.utils import timezone
from django.core.validators import ip_address_validator_map
from rest_framework import status
from rest_framework.views import APIView
from .models import Info
# from .serializers import InfoSerializer
from .serializers import InfoModelSerializer
from rest_framework.response import Response
# from rest_framework import status


class InfoClassBasedViews(APIView):

    def get(self, request, *args, **kwargs):
        qs = Info.objects.all()

        serializer = InfoModelSerializer(instance=qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        current_time = timezone.now()
        context = {
            'current_time': current_time
        }
        print("Current Time", current_time)
        serializer = InfoModelSerializer(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response({
            'method': 'POST',
            'status': 'ok',
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)
