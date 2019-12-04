from django.shortcuts import render, HttpResponse, redirect, reverse 
from django.conf import settings
import stripe 
from django.contrib import messages
from .forms import OrderForm, PaymentForm
from django.utils import timezone

# Create your views here.

def add_request(request):
    return render(request, 'payment/confirm.template.html')

def charge(request):
    if request.method == 'GET':
        
        get_cost = request.GET['cost']
        cost = int(float(get_cost)*100)
        return render(request, 'payment/charge.template.html', {
            'publishable' : settings.STRIPE_PUBLISHABLE_KEY,
            'payment_form' : PaymentForm(),
            'order_form' : OrderForm(),
            'cost': cost,
            'get_cost':get_cost
        })



    else:
        stripeToken = request.POST['stripe_id']
        
        # set the secret key for the Stripe API
        stripe.api_key = settings.STRIPE_SECRET_KEY
        
        order_form = OrderForm(request.POST, request.FILES)
        payment_form = PaymentForm(request.POST)
        
        if order_form.is_valid() and payment_form.is_valid():
            try:
                customer = stripe.Charge.create(
                    amount= int(request.POST['cost']),
                    currency='usd',
                    description='Payment',
                    card=stripeToken
                    )
                    
                if customer.paid:
                    
                    order = order_form.save(commit=False)
                    order.cost=request.POST['cost']
                    order.requester=request.user
                    order.date=timezone.now()
                    order.save()
                    
                    return redirect('/payment/request-run/')
                else:
                    messages.error(request, "Your card has been declined")
            except stripe.error.CardError:
                    messages.error(request, "Your card was declined!")
            
        else:
             return render(request, 'payment/charge.template.html', {
            'order_form' : order_form,
            'payment_form' : payment_form,
            # 'cost' : cost,
            'publishable': settings.STRIPE_PUBLISHABLE_KEY
        })
        
        return render(request, 'payment/charge.template.html', {
            'order_form' : order_form,
            'payment_form' : payment_form,
            # 'cost' : cost,
            'publishable': settings.STRIPE_PUBLISHABLE_KEY
            })   
