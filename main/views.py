from django.shortcuts import render, HttpResponse

# Create your views here.

def request_run(request):
    return HttpResponse("Request Page")
    

def relief_run(request):
    return HttpResponse("Relief Page")