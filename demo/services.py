import os 
import json
import urllib.request
import requests
import psycopg2
from psycopg2.extras import execute_values

def generate_request(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()

def get_user(params={}):

    response = generate_request('https://randomuser.me/api', params)
    user = response.get('results')[0]  
    return user 

def get_many_user(params={}):
    user_list = [] #store all variables into list

    for i in range(6):  #we can change the range value to get more data
        response = generate_request('https://randomuser.me/api', params)
        user = response.get('results')[0]  
        user_list.append(user)
        i +=1
    return user_list 
