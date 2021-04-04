import os 
import requests
import json
import psycopg2
import json, urllib.request
from psycopg2.extras import execute_values

#/demo/views.py
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
# relative import of forms
from .models import userModel
from .forms import userForm
from .services import get_user # services baglantisi

def user_list(request):
    context = {'user_list': userModel.objects.all().order_by("-id")}
    return render(request, "user_list.html", context)

#insert and update operations- GET/POST
def user_form(request, id=0):   

    user = get_user() # service'den randomuser.me ile veri al.
    if request.method == "GET":

        initial_dict = {
        "name" : user.get('name').get('first') + ' ' + user.get('name').get('last'),
        "email":user.get('email'),
        "phone": user.get('phone') 
          }

        if id == 0:
            form = userForm(initial = initial_dict)
        else:
            userr = userModel.objects.get(pk=id)
            form = userForm(instance=userr, initial = initial_dict)
        return render(request,"user_form.html",{'form': form})
    else:
        if id == 0:
            form = userForm(request.POST)
        else:
            userr = userModel.objects.get(pk=id)
            form = userForm(request.POST,instance= userr)        
        if form.is_valid():
            form.save()
        return redirect('/list')

def user_delete(request,id):
    userr = userModel.objects.get(pk=id)
    userr.delete()
    return redirect('/list')