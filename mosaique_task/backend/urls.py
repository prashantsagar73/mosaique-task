from django.urls import path,include
from rest_framework import routers
from .views import *
from .models import *

router = routers.DefaultRouter()
# router.register(r'content', ImageViewset,basename='gallery')
# router.register(r'gallery', VideoViewset,basename='gallery')


urlpatterns = [
    path('data',getWeatherdata),
    # path('get-all-video/',getvideo),
    path('',include(router.urls)),
]