import requests
import json
import csv
import pandas as pd
import datetime as dt
import os


payload = {
        'refresh_token' : "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        'client_id' : 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        "client_secret" : "XXXXXXXXXXXXXXXXXXX",
        'grant_type' : 'refresh_token',
        }

r_token = requests.post('https://oauth2.googleapis.com/token',data=payload).json()

print(r_token)

gfit_access_token = r_token["access_token"] 

print(gfit_access_token)


for i in range(60,91):

    start = dt.datetime.combine(dt.date.today(), dt.datetime.min.time()) - dt.timedelta(days = i)
    start_millis = int(start.timestamp() * 1000)
    
    end = dt.datetime.combine(dt.date.today(), dt.datetime.min.time()) - dt.timedelta(days = i-1) 
    end_millis = int(end.timestamp() * 1000)

    date = str(dt.date.today() - dt.timedelta(days = i))
    print(start_millis)
    print(end_millis)

    firstname = "Pavan"
    lastname = "Kumar"
    phone = "NA"
    email = "NA"
    
    header = {'Content-type': 'application/json',
            'Authorization': 'Bearer ' + gfit_access_token
            }
    
    
    #DATA FETCH --------------------------------------------------------------------------------------

    
    
    #STEPS -------------------------------------------------------------------------------------------

    

    payload = {
            "aggregateBy": [{
                "dataTypeName": "com.google.step_count.delta",
            }],
            "bucketByTime": { "durationMillis": 86400000},
            "startTimeMillis": start_millis,
            "endTimeMillis":  end_millis
            }

    r_token = requests.post('https://www.googleapis.com/fitness/v1/users/me/dataset:aggregate', headers = header, data=json.dumps(payload)).json()
    
    
    checkval = 0
    
    for item in r_token["bucket"]:
        print(item)
        try:
            checkval = int(item["dataset"][0]["point"][0]["value"][0]["intVal"])
        except:
         None
    
    if checkval != 0:
        payload = {
                "aggregateBy": [{
                    "dataTypeName": "com.google.step_count.delta",
                }],
                "bucketByTime": { "durationMillis": 60000},
                "startTimeMillis": start_millis,
                "endTimeMillis":  end_millis
                }

        r_token = requests.post('https://www.googleapis.com/fitness/v1/users/me/dataset:aggregate', headers = header, data=json.dumps(payload)).json()


        # print(r_token)
        gfit_steps = []
        gfit_dates = []

        for item in r_token["bucket"]:
            gfit_dates.append(str(dt.datetime.fromtimestamp(int(item["startTimeMillis"])/1000.0))[10:])
            if len(item["dataset"][0]["point"]) == 0:
                gfit_steps.append(0)
            else:
                gfit_steps.append(item["dataset"][0]["point"][0]["value"][0]["intVal"])
                
        os.makedirs(os.path.dirname("gfit_data/"+firstname+lastname+"_intraday_steps_"+date+".csv"), exist_ok=True)
        with open("gfit_data/"+firstname+lastname+"_intraday_steps_"+date+".csv", 'w') as csvfile:
            writer = csv.writer(csvfile, lineterminator = '\n')
            writer.writerow(["Firstame", firstname])
            writer.writerow(["Lastame", lastname])
            writer.writerow(["Phone", phone])
            writer.writerow(["Email", email])
            writer.writerow(["Token", gfit_access_token])
            writer.writerow(["Date", date])
            writer.writerow(["Datatype", "Intraday Steps"])
            writer.writerow(["", ""])
            writer.writerow(["Time", "Steps"])
            for i in range(len(gfit_dates)):
                writer.writerow([gfit_dates[i], gfit_steps[i]])
            
    #CALORIES -----------------------------------------------------------------------------------------


    header = {'Content-type': 'application/json',
            'Authorization': 'Bearer ' + gfit_access_token
            }

    payload = {
            "aggregateBy": [{
                "dataTypeName": "com.google.calories.expended",
            }],
            "bucketByTime": { "durationMillis": 86400000},
            "startTimeMillis": start_millis,
            "endTimeMillis":  end_millis
            }

    r_token = requests.post('https://www.googleapis.com/fitness/v1/users/me/dataset:aggregate', headers = header, data=json.dumps(payload)).json()
    
    
    checkval = 0
    
    for item in r_token["bucket"]:
        print(item)
        try:
            checkval = int(item["dataset"][0]["point"][0]["value"][0]["fpVal"])
        except:
         None
    
    if checkval != 0:
        payload = {
                "aggregateBy": [{
                    "dataTypeName": "com.google.calories.expended",
                }],
                "bucketByTime": { "durationMillis": 60000},
                "startTimeMillis": start_millis,
                "endTimeMillis":  end_millis
                }

        r_token = requests.post('https://www.googleapis.com/fitness/v1/users/me/dataset:aggregate', headers = header, data=json.dumps(payload)).json()


        # print(r_token)
        gfit_steps = []
        gfit_dates = []

        for item in r_token["bucket"]:
            gfit_dates.append(str(dt.datetime.fromtimestamp(int(item["startTimeMillis"])/1000.0))[10:])
            if len(item["dataset"][0]["point"]) == 0:
                gfit_steps.append(0)
            else:
                gfit_steps.append(item["dataset"][0]["point"][0]["value"][0]["fpVal"])
                
        os.makedirs(os.path.dirname("gfit_data/"+firstname+lastname+"_intraday_calories_"+date+".csv"), exist_ok=True)
        with open("gfit_data/"+firstname+lastname+"_intraday_calories_"+date+".csv", 'w') as csvfile:
            writer = csv.writer(csvfile, lineterminator = '\n')
            writer.writerow(["Firstame", firstname])
            writer.writerow(["Lastame", lastname])
            writer.writerow(["Phone", phone])
            writer.writerow(["Email", email])
            writer.writerow(["Token", gfit_access_token])
            writer.writerow(["Date", date])
            writer.writerow(["Datatype", "Intraday calories"])
            writer.writerow(["", ""])
            writer.writerow(["Time", "Calories"])
            for i in range(len(gfit_dates)):
                writer.writerow([gfit_dates[i], gfit_steps[i]])

    # #ACTIVE MINUTES ------------------------------------------------------------------------------------------

    # payload = {
            # "aggregateBy": [{
                # "dataTypeName": "com.google.active_minutes",
            # }],
            # "bucketByTime": { "durationMillis": 86400000},
            # "startTimeMillis": start_millis,
            # "endTimeMillis":  end_millis
            # }

    # r_token = requests.post('https://www.googleapis.com/fitness/v1/users/me/dataset:aggregate', headers = header, data=json.dumps(payload)).json()

    # gfit_active_mins = []

    # for item in r_token["bucket"]:
        
        # if len(item["dataset"][0]["point"]) == 0:
            # gfit_active_mins.append(0)
        # else:
            # gfit_active_mins.append(item["dataset"][0]["point"][0]["value"][0]["intVal"])


    # #HEARTRATE --------------------------------------------------------------------------------------------------

    checkval = 0
    
    payload = {
            "aggregateBy": [{
                "dataTypeName": "com.google.heart_rate.bpm",
            }],
            "bucketByTime": { "durationMillis": 86400000},
            "startTimeMillis": start_millis,
            "endTimeMillis":  end_millis
            }

    r_token = requests.post('https://www.googleapis.com/fitness/v1/users/me/dataset:aggregate', headers = header, data=json.dumps(payload)).json()

    for item in r_token["bucket"]:
        print(item)
        try:
            checkval = int(item["dataset"][0]["point"][0]["value"][0]["fpVal"])
        except:
         None
            
    if checkval != 0:        
        payload = {
                "aggregateBy": [{
                    "dataTypeName": "com.google.heart_rate.bpm",
                }],
                "bucketByTime": { "durationMillis": 60000},
                "startTimeMillis": start_millis,
                "endTimeMillis":  end_millis
                }

        r_token = requests.post('https://www.googleapis.com/fitness/v1/users/me/dataset:aggregate', headers = header, data=json.dumps(payload)).json()


        gfit_dates = []
        gfit_hr = []
        for item in r_token["bucket"]:
            gfit_dates.append(str(dt.datetime.fromtimestamp(int(item["startTimeMillis"])/1000.0))[10:])
            if len(item["dataset"][0]["point"]) == 0:
                gfit_hr.append(0)
            else:
                gfit_hr.append(int(item["dataset"][0]["point"][0]["value"][0]["fpVal"]))
                
        print(gfit_dates)
        print(gfit_hr)
        
        os.makedirs(os.path.dirname("gfit_data/"+firstname+lastname+"_intraday_heartrate_"+date+".csv"), exist_ok=True)
        with open("gfit_data/"+firstname+lastname+"_intraday_heartrate_"+date+".csv", 'w') as csvfile:
            writer = csv.writer(csvfile, lineterminator = '\n')
            writer.writerow(["Firstame", firstname])
            writer.writerow(["Lastame", lastname])
            writer.writerow(["Phone", phone])
            writer.writerow(["Email", email])
            writer.writerow(["Token", gfit_access_token])
            writer.writerow(["Date", date])
            writer.writerow(["Datatype", "Intraday Heartrate"])
            writer.writerow(["", ""])
            writer.writerow(["Time", "HeartRate"])
            for i in range(len(gfit_dates)):
                if gfit_hr[i] != 0:
                    writer.writerow([gfit_dates[i], gfit_hr[i]])
  