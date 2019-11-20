from django.urls import path, include
from .views import request_run, relief_run, request_info 


urlpatterns = [
    path('request-run/', request_run, name='request-run'),
    path('relief-run', relief_run, name='relief-run'),
    path('request-info', request_info, name='request-info'),
    # path('add-request',add_request, name='add-request')
    path('payment/',include('payment.urls'))
   
    
]