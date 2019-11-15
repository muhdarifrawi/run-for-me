from django.urls import path, include
from .views import request_run, relief_run


urlpatterns = [
    path('request-run/', request_run, name='request-run'),
    path('relief-run', relief_run, name='relief-run')
    
]