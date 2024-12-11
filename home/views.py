from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("this is homepage")

def about(request):
    return HttpResponse("this is aboutPage")

def Services(Services):
    return HttpResponse("this is Services Section")

def Contact(Contact):
    return HttpResponse("this is contact Section")