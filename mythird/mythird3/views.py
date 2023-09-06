from django.shortcuts import render,HttpResponse
from .models import student

# Create your views here.

def index (request):
    return render(request,'index.html')

def contact (request):
    return render(request,'contact.html')

def index1(request):
    return render(request,'index1.html')

def form(request):
    return render(request,'form.html')

def corousel(request):
    return render(request,'corousel.html')

def button (request):
    return render(request,'button.html')

def resume (request):
    return render (request,'resume')


def index3(request):
    data=student.objects.all()
    
    for i in data:
        print(i)
    print(data)
    context ={
        'd' :data
    }        
    return render(request,'index3.html',context)


