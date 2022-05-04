from urllib import response
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def products(request):
    products = ['iphone','oppo', 'samsung', 'huawei']
    return HttpResponse(products)