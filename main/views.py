from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib import messages
from payment.models import orders
from django.conf import settings
import stripe 

# Create your views here.
# this is the main views. do not put any payment stuff here.

def request_run(request):
    # all_orders = orders.objects.all();
    personal_orders = orders.objects.filter(requester=request.user);
    return render(request, "request-run.template.html",{
        'personal_orders':personal_orders
    })
    
def request_info(request):
    personal_orders = orders.objects.filter(requester=request.user);
    return render(request, "request-info.template.html",{
        'personal_orders':personal_orders
    })
    

def relief_run(request):
    all_orders = orders.objects.all();
    return render(request, "relief-run.template.html",{
        'all_orders':all_orders
    })

    
