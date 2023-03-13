from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def virat(request):
    return HttpResponse('<h1><marquee>virat is a best batsman in the world</marquee></h1>')