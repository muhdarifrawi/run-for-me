from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib import messages
from .models import orders
from .forms import addRequestForm


# Create your views here.

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
    
def add_request(request):
    form = addRequestForm()
    if request.method == 'POST':
        form = addRequestForm(request.POST)
        
        if form.is_valid():
        
            new_request = form.save(commit=False)
            new_request.requester = request.user
            new_request.save()
            messages.success(request,"You request has been submitted")
            return redirect(reverse("request-run"))
        
        else:
            messages.error(request,"Sorry.Something went wrong.")
        
    else: 
        return render(request, "add-request.template.html", {
            'form':form
        })
        

def relief_run(request):
    all_orders = orders.objects.all();
    return render(request, "relief-run.template.html",{
        'all_orders':all_orders
    })

    
