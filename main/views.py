from django.shortcuts import render, HttpResponse

# Create your views here.

def request_run(request):
    return render(request, "request-run.template.html")
    

def relief_run(request):
    return render(request, "relief-run.template.html")