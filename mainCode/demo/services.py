import os 
import requests
import json
import psycopg2
import json, urllib.request
from psycopg2.extras import execute_values

def generate_request(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()

def get_username(params={}):

    user_list = [] #store all variables into list
    try:
        conn = psycopg2.connect(host="localhost", port ='', database='prodaft', user='postgres', password='prodaft123*')
    except:
        print("I am unable to connect to the database")

    cur = conn.cursor()

    for i in range(6):  #we can change the range value to get more data
        response = generate_request('https://randomuser.me/api', params)
        user = response.get('results')[0]  
        user_list.append(user)
        i +=1

        # ***** connect to the db *******


    fields = [
        'id', #integer
        'name', #varchar
        'email', #varchar
        'phone', #varchar
        #'location.city', #varchar
    ]

    for item in user_list:
        my_data = [item[field] for field in fields]
        insert_query = "INSERT INTO tableprodaft VALUES (%d, %s, %s, %d)"
        cur.execute(insert_query, dict(my_data))
        conn.commit()

    # close the cursor
    cur.close()

    # close the connection
    conn.close()

    return user_list 

"""    data = {}

    with open('data.json', 'a') as outfile:
        json.dump(user_list, outfile) """