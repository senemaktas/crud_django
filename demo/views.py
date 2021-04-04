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
    if request.method == "GET":
        if id == 0:
            form = userForm()
        else:
            userr = userModel.objects.get(pk=id)
            form = userForm(instance=userr)
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


def fill_form(request):
    userr= userModel()
    userr = userModel.objects.get(pk=id)
    user=get_user()
    userr.name = request.POST.get(user.get('name'))
    userr.email = request.POST.get(user.get('email'))
    userr.phone= request.POST.get(user.get('phone'))
    form = userForm(request.POST,instance= userr)
    if form.is_valid():
        form.save()
    return redirect('/list')

"""def user_create(request, id=0):

    context = {
        'user_add': get_user(params={})   }  #connect service and get data

    try:
        conn = psycopg2.connect(host="localhost", port ='', database='newdb', user='postgres', password='prodaft123*')
    except:
        print("I am unable to connect to the database")

    cur = conn.cursor()

    insert_query = "INSERT INTO newtable VALUES (%d, %s, %s, %d)"
    cur.execute(insert_query, dict(user_list))
    conn.commit()

    # close the cursor
    cur.close()

    # close the connection
    conn.close()

    return redirect('/list') """