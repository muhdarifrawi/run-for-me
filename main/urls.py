from django.urls import path, include
from .views import request_run, relief_run, request_info, delete_order
from django.conf.urls.static import static 
from django.conf import settings 

urlpatterns = [
    path('request-run/', request_run, name='request-run'),
    path('relief-run', relief_run, name='relief-run'),
    path('request-info', request_info, name='request-info'),
    path('payment/',include('payment.urls')),
    path('<sku>/delete-order/',delete_order, name='delete-order')
   
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
