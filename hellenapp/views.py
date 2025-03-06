from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def details(request):
    return render(request,'meeting-details.html')

def meet(request):
    return render(request,'meetings.html')
