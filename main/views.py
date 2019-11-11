from django.shortcuts import render, HttpResponse

# Create your views here.

def show_main(request):
    return render(request, "index.template.html")
