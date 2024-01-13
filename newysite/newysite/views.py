from django.http import HttpResponse
from django.shortcuts import render
from services.models import Service
data={}
def Home (request):
    data={}
    servicedata=Service.objects.all()
    if request.method=="GET":
        st=request.GET.get("servicetitle")
        if st!=None:
            servicedata=Service.objects.filter(service_title__icontains=st)

    data={
        "servicedata":servicedata
    }
    return render (request,"home.html",data)

def userform (request):
    data={}
    try:
        if request.method=="POST":
            n1=int(request.POST.get("num1"))
            n2=int(request.POST.get("num2"))
            finalans=n1+n2
            data={
                "finalans":finalans
            }
    except:
        pass
    return render(request,"forms.html",data)

def homepage (request):
    data={
        'title':"Home New",
        'bdata':"This is Hammad khan from Nowshera",
        'list':['Java','python','django'],
        'numbers':[10,20,30,40,50,60]
    }
    return render (request,"index.html",data)

def about (request):
    return render (request, "about.html")

def contact (request):
    return render (request, "contact.html")

def contactDetails (request,contdetails):
    return HttpResponse(contdetails)