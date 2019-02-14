from django.http import HttpResponse
from django.shortcuts import render

from .models import Customer

# Create your views here.
def index(request):
    return HttpResponse("Project 3: TODO")
