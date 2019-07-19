from django.urls import path
from .views import *

urlpatterns = [
    path('' , index , name = 'index'),
    path('placeapi', Get_place_List.as_view())
]