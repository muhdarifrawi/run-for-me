from django.urls import path
from .views import add_request, charge
from main.views import request_run

urlpatterns = [
    # path("confirm/", confirmation, name="confirm"),
    path("charge/", charge, name="charge"),
    path('add-request',add_request, name='add-request'),
    path('request-run/', request_run, name='request-run')
]