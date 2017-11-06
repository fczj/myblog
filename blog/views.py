from django.shortcuts import render,HttpResponse
import logging

# Create your views here.


def index(request):
    return render(request,'index.html')
