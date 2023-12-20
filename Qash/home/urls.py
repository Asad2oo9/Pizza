from django.urls import path
from home.views import *

urlpatterns = [
    path("weather/", index , name="weather"),
    path('history/', history, name='history'),
]