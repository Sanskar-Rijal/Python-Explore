from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
   # return HttpResponse("this is homepage")
   context={
    "variable1":"this is sent",
    "variable2":"Sanskar is pro"
   }
   return render(request,'index.html',context)

def about(request):
    #return HttpResponse("this is aboutPage")
    return render(request,'about.html')

def Services(Services):
   # return HttpResponse("this is Services Section")
   return render(Services,'services.html')

def Contact(Contact):
    #return HttpResponse("this is contact Section")
    return render(Contact,'contact.html')