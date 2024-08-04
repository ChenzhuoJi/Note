from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    """
    网页的样子
    """
    return HttpResponse("Hello, world. You're at the polls index.")