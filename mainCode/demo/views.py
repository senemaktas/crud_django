#/demo/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

"""def index(request):
    return HttpResponse("<h1>Hello, world i am senem!</h1>") """
 
        
from .services import get_username

def index(request):
    params = { 'order': 'desc' }

    context = {
        'UserInfos': get_username(params) # define UserInfos in home.html
    }
    return render(request,'home.html', context)
