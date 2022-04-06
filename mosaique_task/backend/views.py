from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response



# Create your views here.
class watherViewset(viewsets.ModelViewSet):
    # permission_classes=[ReadOnly]
    serializer_class = weatherSerializer
    pagination_class=None
    def get_queryset(self):
        if self.request.user.is_staff:
            return Weather.objects.filter(batch__teacher__user=self.request.user).distinct()
        
@api_view(['Get'])
# @permission_classes([AllowAny])
def getWeatherdata(request):
    # gallerys = gallery.objects.filter(main='id').order_by('id')
    contents = Weather.objects.order_by('id')
    serializer = weatherSerializer(contents,many=True)
    return Response(serializer.data) 