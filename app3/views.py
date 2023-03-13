from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def dhoni(request):
    return HttpResponse('<h1>dhoni is a great finisher in the world</h1>')
