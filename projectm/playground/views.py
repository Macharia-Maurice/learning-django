from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    name={'name':'Maurice'}
    
    return render(request,'hello.html', name)