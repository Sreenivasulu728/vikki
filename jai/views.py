from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def wishes(request):
    return HttpResponse('Hi Nivas this is django_response')

def Birthday(request):
    
    return HttpResponse('<h1><marquee>Happy birthday django</marquee></h1>')

# def even(request):
#     a=10
#     if a%2==0:
#         return 'prime'    
#     return HttpResponse('Not prime')