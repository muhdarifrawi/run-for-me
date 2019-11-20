from django.shortcuts import render, HttpResponse, redirect, reverse 
from django.conf import settings
import stripe 
from django.contrib import messages
from .models import orders
from .forms import addRequestForm

# Create your views here.

def confirmation(request):
    form = addRequestForm()
    return render(request, "payment/confirm.template.html",{'form':form})
    
    
# def charge(request):
#     if request.method == 'GET': 
#         form = addRequestForm()
#         amount = request.GET['amount'] 
#         stripe_publishable_key = settings.STRIPE_PUBLISHABLE_KEY
#         return render(request, 'payment/charge.template.html', {
#                 'publishable_key':stripe_publishable_key,
#                 'amount_in_dollars':amount,
#                 'amount':int(amount)*100
#             })
#         # return HttpResponse("here")
#     else:
#         stripe.api_key = settings.STRIPE_SECRET_KEY
#         stripe_token = request.POST["stripeToken"]
#         charge = stripe.Charge.create(amount=request.POST["amount"],
#             currency='usd',
#             source=stripe_token
#         )
#         return HttpResponse("Submitted")

#charge and add request (this is a new function)
def charge(request):
    form = addRequestForm()
    if request.method == 'GET':
        form = addRequestForm(request.GET)
        sku = request.GET['sku']
        bid = request.GET['bid']
        cost = request.GET['cost']
        due_date_month = request.GET['due_date_month']
        due_date_day = request.GET['due_date_day']
        due_date_year = request.GET['due_date_year']
        stripe_publishable_key = settings.STRIPE_PUBLISHABLE_KEY
        return render(request, 'payment/charge.template.html', {
                'publishable_key':stripe_publishable_key,
                'sku':sku,
                'bid':bid,
                'cost':cost,
                'due_date_month':due_date_month,
                'due_date_day':due_date_day,
                'due_date_year':due_date_year,
                'form':form
            })
        
    else: 
        
        form = addRequestForm(request.POST)
        
        if form.is_valid():
        
            new_request = form.save(commit=False)
            new_request.requester = request.user
            new_request.save()
            messages.success(request,"Your request has been submitted")
            return redirect(reverse("request-run"))
        
        else:
            # messages.error(request,"Sorry.Something went wrong.")
            # return render(request,'main/request-run.template.html')
            return HttpResponse("okay can")