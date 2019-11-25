from django.shortcuts import render, HttpResponse, redirect, reverse 
from django.conf import settings
import stripe 
from django.contrib import messages
from .forms import OrderForm, PaymentForm

# Create your views here.

def add_request(request):
    return render(request, 'payment/confirm.template.html')

def charge(request):
    if request.method == 'GET':
        #show form
        return render(request, 'payment/charge.template.html', {
            'publishable' : settings.STRIPE_PUBLISHABLE_KEY,
            'payment_form' : PaymentForm(),
            'order_form' : OrderForm(),
            'cost': request.GET['cost']
        })
    
# def charge(request):
#     if request.method == 'GET':
        
        
#         stripe_publishable_key = settings.STRIPE_PUBLISHABLE_KEY
    
#         cost = request.GET['cost'] 
#         return render(request, 'payment/charge.template.html', {
#                 'publishable_key':stripe_publishable_key,
#                 'cost_in_dollars':cost,
#                 'cost':int(cost)*100
#             })
    
#     else:
        
#         messages.success(request,"Your request has been submitted.")
    
#         stripe.api_key = settings.STRIPE_SECRET_KEY
#         stripe_token = request.POST["stripeToken"]
#         charge = stripe.Charge.create(amount=request.POST["cost"],
#             currency='usd',
#             source=stripe_token
#         )
#         return redirect(reverse, ("request-run"))
 