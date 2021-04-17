import os 
import requests
import json
import psycopg2
import json, urllib.request
from psycopg2.extras import execute_values

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import userModel #relative import of forms
from .forms import userForm
from .services import get_user #services baglantisi

from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.parsers import JSONParser 
from rest_framework import status
from demo.serializers import userSerializer
from rest_framework.decorators import api_view

@api_view(['GET','DELETE'])
def user_list(request):
    context = {'user_list': userModel.objects.all().order_by("-id")}
    serializer = userSerializer(context, many=True)
    return render(request, "user_list.html", context)


@api_view(['GET', 'POST'])
#insert and update operations- GET/POST
def user_form(request, id=0):   

    user = get_user() # service'den randomuser.me ile veri al.
    serializer = userSerializer(data=request.data)
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
            #serializer = userSerializer(instance=userr, data=request.data) 
        if form.is_valid() and serializer.is_valid():
            form.save()
            serializer.save()

        return redirect('/list')

@api_view(['DELETE'])
def user_delete(request,id):
    userr = userModel.objects.get(pk=id)
    userr.delete()
    return redirect('/list')
