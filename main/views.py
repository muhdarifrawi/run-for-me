from django.shortcuts import render, HttpResponse

# Create your views here.

def show_main(request):
    return HttpResponse("Hello world")
