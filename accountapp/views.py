from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_again(request):
    return render(request,'accountapp/hello_again.html')