from django.urls import path, include
from .views import confirmation, charge

urlpatterns = [
    path('confirm/', confirmation, name='confirm'),
    path("charge/", charge, name="charge")
    
]