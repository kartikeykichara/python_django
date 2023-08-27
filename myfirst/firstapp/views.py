from django.shortcuts import render

# Create your views here.
def output(request):
    return render(request,'instagram.html')

def neww(request):
    return render(request,'neww.html')

def catering1(request):
    return render(request,'catering1.html')

def catering2(request):
    return render(request,'catering2.html')