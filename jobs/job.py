from django.conf import settings
import datetime as dt
import boto3
from boto3.dynamodb.conditions import Key
import csv
import requests
import json
import os
from django.core.mail import send_mail


def schedule_fetch():
    date= str(dt.datetime.now())
    print(date)
    dd = 2
    dynamodb= boto3.resource('dynamodb',region_name='ap-south-1',aws_access_key_id='xxxxxxx',aws_secret_access_key='xxxxxxxxxxxxx')
    tableuser = dynamodb.Table('cure_trial')
    response = tableuser.scan()    
    items = response['Items']


    for item in items:
        access_token = item['token']
        name = item['name']
        phone = item['phone'] 
        try:
            print(item['count'])
        except:
            tableuser.put_item(Item= {'timestamp': item["timestamp"],
                                      'email':  item["email"],
                                      'firstname' : item["firstname"],
                                      'lastname' : item["lastname"],
                                      'name' : item["name"],
                                      'phone' : item["phone"],
                                      'token' : item["token"],
                                      'count' : 0,               
                                      })
            
        os.makedirs(os.path.dirname("fitbit_data/"+ name + phone +"/"+ name + phone +"patientinfo.txt"), exist_ok=True)
        with open("fitbit_data/"+ name + phone +"/"+ name + phone +"patientinfo.txt", 'w') as f:
            f.write('Firstname: ' + item['firstname'] + "\n")
            f.write('Lastname: ' + item['lastname'] + "\n")
            f.write('Phone: ' + item['phone'] + "\n")
            f.write('Email: ' + item['email'] + "\n")
            f.write('Token: ' + item['token'] + "\n")

        header = {'accept': 'application/x-www-form-urlencoded','Authorization': 'Bearer {}'.format(access_token)}
        
        today = dt.date.today()

        date = str(today - dt.timedelta(days = dd))

        response = requests.get("https://api.fitbit.com/1/user/-/activities/heart/date/"+date+"/1d/1sec.json", headers=header).json()
        
        dates=[]
        values=[]
        


        
        try:
            #HeartRate
            steps_intraday = response['activities-heart-intraday']['dataset']
            if len(steps_intraday) > 1:
                
                os.makedirs(os.path.dirname("fitbit_data/"+ name + phone +"/"+ name + phone +"intraday_heartrate_"+date+".csv"), exist_ok=True)
                os.makedirsedirs(os.path.dirname("fitbit_data/"+ name + phone +"/"+ name + phone +"heartrate_summary_"+date+".csv"), exist_ok=True)
                for line in steps_intraday:
                    dates.append(line['time'][0:8])
                    values.append(line['value'])
                
                with open("fitbit_data/"+ name + phone +"/"+ name + phone +"intraday_heartrate_"+date+".csv", 'w') as csvfile:
                    writer = csv.writer(csvfile, lineterminator = '\n')
    ##                writer.writerow(["Firstame", item['firstname']])
    ##                writer.writerow(["Lastame", item['lastname']])
                    writer.writerow(["Phone", item['phone']])
    ##                writer.writerow(["Email", item['email']])
    ##                writer.writerow(["Token", item['token']])
    ##                writer.writerow(["Date", date])
                    writer.writerow(["Datatype", "Intraday Heartrate"])
                    writer.writerow(["", ""])
                    writer.writerow(["Time", "HeartRate"])
                    for i in range(len(dates)):
                        writer.writerow([dates[i], values[i]])
                with open("fitbit_data/"+ name + phone +"/"+ name + phone +"heartrate_summary_"+date+".csv", 'w') as csvfile:
                    writer = csv.writer(csvfile, lineterminator = '\n')
    ##                writer.writerow(["Firstame", item['firstname']])
    ##                writer.writerow(["Lastame", item['lastname']])
                    writer.writerow(["Phone", item['phone']])
    ##                writer.writerow(["Email", item['email']])
    ##                writer.writerow(["Token", item['token']])
    ##                writer.writerow(["Date", date])
                    writer.writerow(["Datatype", "Daily Heartrate Summary"])
                    writer.writerow(["", ""])
                    writer.writerow(["Heart Rate Zone", "Calories Out", "Max HeartRate", "Min HeartRate", "Minutes"])
                    for line in response['activities-heart'][0]['value']['heartRateZones']:
                        writer.writerow([ line["name"],line["caloriesOut"],line["max"],line["min"],line["minutes"]])
                tableuser.put_item(Item= {'timestamp': item["timestamp"],
                                      'email':  item["email"],
                                      'firstname' : item["firstname"],
                                      'lastname' : item["lastname"],
                                      'name' : item["name"],
                                      'phone' : item["phone"],
                                      'token' : item["token"],
                                      'count' : 0,               
                                      })
            else:
                tableuser.put_item(Item= {'timestamp': item["timestamp"],
                                      'email':  item["email"],
                                      'firstname' : item["firstname"],
                                      'lastname' : item["lastname"],
                                      'name' : item["name"],
                                      'phone' : item["phone"],
                                      'token' : item["token"],
                                      'count' : item["count"]+ 1,            
                                      })
                         
        except:
                None

        date = str(today - dt.timedelta(days = dd))

        dates = []
        steps_values = []
        calories_values = []
        elevation_values = []

        response = requests.get("https://api.fitbit.com/1/user/-/activities/steps/date/"+date+"/1d/1min.json", headers=header).json()
        

        try:
            steps_intraday = response['activities-steps-intraday']['dataset']
            for line in steps_intraday:
                dates.append(line['time'][0:5])
                steps_values.append(line['value'])
                
            response = requests.get("https://api.fitbit.com/1/user/-/activities/calories/date/"+date+"/1d/1min.json", headers=header).json()
            steps_intraday = response['activities-calories-intraday']['dataset']
            for line in steps_intraday:
                calories_values.append(line['value'])
                
            response = requests.get("https://api.fitbit.com/1/user/-/activities/elevation/date/"+date+"/1d/1min.json", headers=header).json()
            steps_intraday = response['activities-elevation-intraday']['dataset']
            for line in steps_intraday:
                elevation_values.append(int(line['value'])*10)

            os.makedirs(os.path.dirname("fitbit_data/"+ name + phone +"/"+ name + phone +"intraday_steps_cal_elev_"+date+".csv"), exist_ok=True)

            with open("fitbit_data/"+ name + phone +"/"+ name + phone +"intraday_steps_cal_elev_"+date+".csv", 'w') as csvfile:
                writer = csv.writer(csvfile, lineterminator = '\n')
##                writer.writerow(["Name", item['name']])
                writer.writerow(["Phone", item['phone']])
##                writer.writerow(["Email", item['email']])
##                writer.writerow(["Token", item['token']])
                writer.writerow(["Datatype", "Intraday Activities"])
                writer.writerow(["", ""])
                writer.writerow(["Time", "Steps","Calories","Elevation(m)"])
                for i in range(len(dates)):
                    writer.writerow([dates[i], steps_values[i], calories_values[i], elevation_values[i]])

        except:
            None

        date = str(today - dt.timedelta(days = dd))
        response = requests.get("https://api.fitbit.com/1.2/user/-/sleep/date/"+date+".json", headers=header).json()
        
        

        dates = []
        values = []
        sleep_levels = []

        try:
            steps = response['sleep']
            intra = steps[0]['levels']['data']
            for line in intra:
                dates.append(line['dateTime'])
                values.append(int(int(line['seconds'])/60))
                sleep_levels.append(line['level'])

            os.makedirs(os.path.dirname("fitbit_data/"+ name + phone +"/"+ name + phone +"intraday_sleep_"+date+".csv"), exist_ok=True)

            with open("fitbit_data/"+ name + phone +"/"+ name + phone +"intraday_sleep_"+date+".csv", 'w') as csvfile:
                writer = csv.writer(csvfile, lineterminator = '\n')
##                writer.writerow(["Firstame", item['firstname']])
##                writer.writerow(["Lastame", item['lastname']])
                writer.writerow(["Phone", item['phone']])
##                writer.writerow(["Email", item['email']])
##                writer.writerow(["Token", item['token']])
##                writer.writerow(["Date", date])
                writer.writerow(["Datatype", "Intraday Sleep"])
                writer.writerow(["", ""])
                writer.writerow(["Timestamp", "Minutes Asleep", "Sleep Type"])
                for i in range(len(dates)):
                    writer.writerow([dates[i], values[i], sleep_levels[i]])

        except:
            None

        date = str(today - dt.timedelta(days = dd))
        response = requests.get("https://api.fitbit.com/1/user/-/activities/date/"+date+".json", headers=header).json()
        

        try:
            os.makedirs(os.path.dirname("fitbit_data/"+ name + phone +"/"+ name + phone +"activity_summary_"+date+".csv"), exist_ok=True)

            with open("fitbit_data/"+ name + phone +"/"+ name + phone +"activity_summary_"+date+".csv", 'w') as csvfile:
                writer = csv.writer(csvfile, lineterminator = '\n')
##                writer.writerow(["Firstame", item['firstname']])
##                writer.writerow(["Lastame", item['lastname']])
                writer.writerow(["Phone", item['phone']])
##                writer.writerow(["Email", item['email']])
##                writer.writerow(["Token", item['token']])
##                writer.writerow(["Date", date])
                writer.writerow(["Datatype", "Daily Activity Summary"])
                writer.writerow(["", ""])
                
                for key, value in response["summary"].items():
                    if key != "distances" and key != "heartRateZones":
                        writer.writerow([key, value])

                writer.writerow(["", ""])
                writer.writerow(["Activity Type", "Distance(km)"])
                for line in response["summary"]["distances"]:
                    writer.writerow([line["activity"], line["distance"]])

        except:
            None

        date = str(today - dt.timedelta(days = dd))
        response = requests.get("https://api.fitbit.com/1/user/-/profile.json", headers=header).json()
        

        try:
            os.makedirs(os.path.dirname("fitbit_data/"+ name + phone +"/"+ name + phone +"user_profile.csv"), exist_ok=True)

            with open("fitbit_data/"+ name + phone +"/"+ name + phone +"user_profile.csv", 'w') as csvfile:
                writer = csv.writer(csvfile, lineterminator = '\n')
##                writer.writerow(["Firstame", item['firstname']])
##                writer.writerow(["Lastame", item['lastname']])
                writer.writerow(["Phone", item['phone']])
##                writer.writerow(["Email", item['email']])
##                writer.writerow(["Token", item['token']])
##                writer.writerow(["Date", date])
                writer.writerow(["Datatype", "User Profile"])
                writer.writerow(["", ""])
                
                for key, value in response["user"].items():
                    writer.writerow([key, value])


        except:
            None

