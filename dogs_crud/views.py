from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return HttpResponse('<h1>Welcome to our Dog App! /ᐠ｡‸｡ᐟ\ﾉ</h1>')

# Create your views here.
