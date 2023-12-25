from django.shortcuts import render
from django.http import HttpResponse

def greetings2(request):
    return HttpResponse('Hello again')
