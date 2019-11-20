from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib import messages
from payment.models import orders
from payment.forms import addRequestForm
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
    
# def add_request(request):
#     form = addRequestForm()
#     if request.method == 'GET':
#         amount = request.GET.get('form.cost')
#         stripe_publishable_key = settings.STRIPE_PUBLISHABLE_KEY
#         return render(request, 'payment/charge.template.html', {
#                 'publishable_key':stripe_publishable_key,
#                 'amount_in_dollars':amount,
#                 'amount':amount,
#                 'form':form
#             })
        
#     else: 
        
#         form = addRequestForm(request.POST)
        
#         if form.is_valid():
        
#             new_request = form.save(commit=False)
#             new_request.requester = request.user
#             new_request.save()
#             messages.success(request,"Your request has been submitted")
#             return redirect(reverse("request-run"))
        
#         else:
#             messages.error(request,"Sorry.Something went wrong.")
#             return render(request,'main/request-run.trmplate.html')
        

def relief_run(request):
    all_orders = orders.objects.all();
    return render(request, "relief-run.template.html",{
        'all_orders':all_orders
    })

    
