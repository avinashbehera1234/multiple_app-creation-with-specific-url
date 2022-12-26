from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def avinash(request):
    return HttpResponse('<h2>this is app2 avinash view</h2>')