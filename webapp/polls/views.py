from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World. This is index.")

def detail(request, id_page):
    return HttpResponse("This is detail page %s" % id_page)

def results(request, id_page):
    return HttpResponse("This page shows you results %s" % id_page)

def vote(requst, id_page):
    response = "This page show you votes %s"
    return HttpResponse(response % id_page) 