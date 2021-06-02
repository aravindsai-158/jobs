from django.shortcuts import render
from django.http import HttpResponse
def hydjobs(request):
    s="<h1> Hyderabad Jobs </h1>"
    return HttpResponse(s)

def punejobs(request):
    s="<h1> Pune Jobs </h1>"
    return HttpResponse(s)

def mumbaijobs(request):
    s="<h1> Mumbai Jobs  </h1>"
    return HttpResponse(s)

def banglorejobs(request):
    s="<h1> Banglore Jobs </h1>"
    return HttpResponse(s)
