from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib import messages
from payment.models import orders
from payment.forms import OrderForm
from django.conf import settings
import stripe 

# Create your views here.
# this is the main views. do not put any payment stuff here.

def request_run(request):
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
    
def delete_order(request, sku):
    if request.method == 'GET':
        current_order = sku
        return render(request, "delete.template.html", {
            'current_order':current_order
        })
        
    else:
        orders.objects.filter(sku=sku).delete()
        personal_orders = orders.objects.filter(requester=request.user);
        return render(request, "request-run.template.html",{
            'personal_orders':personal_orders
        })
        
        
def edit_order(request, sku):
    if request.method == 'GET':
        current_order = sku
        order = orders.objects.get(sku=sku)
        form = OrderForm(instance=order)
        # form['full_name'].value()
        return render(request, "edit.template.html", {
            'current_order':current_order,
            'form':form
        })
        
    else:
        order = orders.objects.get(sku=sku)
        form = OrderForm(request.POST,instance=order)
        form.save()
        personal_orders = orders.objects.filter(requester=request.user);
        return render(request, "request-run.template.html",{
            'personal_orders':personal_orders
        })