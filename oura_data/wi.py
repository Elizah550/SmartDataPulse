import requests
import json
import csv
import pandas as pd
import datetime as dt

access_token = "access_token=" + "YVEDEFSOCZWAL4CO7MMO2VEACYPACAFY"

today = dt.date.today()

day = 400
previous = today - dt.timedelta(days = day)
enddate = today
startdate = previous

# response = requests.get("https://api.ouraring.com/v1/sleep?start="+str(startdate)+"&end="+str(enddate)+"&"+access_token).json()
# #print(response)


# for i in range(day):
    # try:
        
        # date = response["sleep"][i]["summary_date"]
        
        
        
        # with open("sleep_heartrate_"+date+".csv", 'w') as csvfile:
            # writer = csv.writer(csvfile, lineterminator = '\n')
            # writer.writerow(["Timestamp", "HeartRate"])
            
            # sleep_start_time = response["sleep"][i-1]["bedtime_start"][:19].replace("T"," ")
            # sleep_start_time = dt.datetime.strptime(sleep_start_time, "%Y-%m-%d %H:%M:%S")
            # print(sleep_start_time, date)
            
            # for value in response["sleep"][i-1]['hr_5min']:
            
                # if date in str(sleep_start_time):
                    # if value != 0:
                        # writer.writerow([str(sleep_start_time), value])
                # sleep_start_time = sleep_start_time + dt.timedelta(minutes = 5)
            
            # sleep_start_time = response["sleep"][i]["bedtime_start"][:19].replace("T"," ")
            # sleep_start_time = dt.datetime.strptime(sleep_start_time, "%Y-%m-%d %H:%M:%S")
            # print(sleep_start_time, date)
            
            # for value in response["sleep"][i]['hr_5min']:
                # if date in str(sleep_start_time):
                    # if value != 0:
                        # writer.writerow([str(sleep_start_time), value])
                # sleep_start_time = sleep_start_time + dt.timedelta(minutes = 5)
                
        # with open("sleep_data_"+date+".csv", 'w') as csvfile:
            # writer = csv.writer(csvfile, lineterminator = '\n')
            # writer.writerow(["Type of Sleep", "duration (minutes)"])
            # writer.writerow(["awake", response["sleep"][i]['awake']/60])
            # writer.writerow(["light", response["sleep"][i]["light"]/60])
            # writer.writerow(["deep", response["sleep"][i]["deep"]/60])
            # writer.writerow(["rem", response["sleep"][i]['rem']/60])
        
    # except:
        # None
 

response = requests.get("https://api.ouraring.com/v1/activity?start="+str(startdate)+"&end="+str(enddate)+"&"+access_token).json()
# print(response)

for i in range(day):
    try:
        
        date = response["activity"][i]["summary_date"]
        
        # with open("intraday_met_"+date+".csv", 'w') as csvfile:
        
            # writer = csv.writer(csvfile, lineterminator = '\n')
            # writer.writerow(["Timestamp", "MET"])
            
            # day_start_time = response["activity"][i-1]["day_start"][:19].replace("T"," ")        
            # day_start_time = dt.datetime.strptime(day_start_time, "%Y-%m-%d %H:%M:%S")        
            # print(date, day_start_time)
            
            
            # for value in response['activity'][i-1]['met_1min']:
                
                # if date in str(day_start_time):
                    # writer.writerow([str(day_start_time), value])
                # day_start_time = day_start_time + dt.timedelta(minutes = 1)
            
            # day_start_time = response["activity"][i]["day_start"][:19].replace("T"," ")        
            # day_start_time = dt.datetime.strptime(day_start_time, "%Y-%m-%d %H:%M:%S")        
            # print(date, day_start_time)
            

            # for value in response['activity'][i]['met_1min']:
                # if date in str(day_start_time):
                    # writer.writerow([str(day_start_time), value])
                # day_start_time = day_start_time + dt.timedelta(minutes = 1)
                
        with open("calories_steps_"+date+".csv", 'w') as csvfile:
        
            writer = csv.writer(csvfile, lineterminator = '\n')
            writer.writerow(["Calories", response['activity'][i]['cal_total']])
            writer.writerow(["Steps", response['activity'][i]['steps']])
            
    except:
        None
# # while len(response2['activity']) == 0:
    # # previous = previous - dt.timedelta(days = 1)
    # # response2 = requests.get("https://api.ouraring.com/v1/activity?start="+str(previous)+"&end="+str(today)+"&"+access_token).json()

# # oura_dates2 = []
# # oura_steps_values = []
# # oura_calories_values = []
# # oura_met_values = []
# # oura_met_intraday = []
# # oura_met_times = []
# # for item in response2['activity']:
    # # oura_dates2.append(item['summary_date'])
    # # oura_steps_values.append(item['steps'])
    # # oura_calories_values.append(item["cal_total"])
    # # oura_met_values.append(item['average_met'])
    # # oura_met_intraday = item["met_1min"]

# # a = dt.datetime.now()    
# # hr = "04"
# # sc = "00"
# # a = a.replace(hour=int(hr),minute=int(sc),second=0)
# # for ab in range(len(oura_met_intraday)):
    # # oura_met_times.append(str(a)[11:16])
    # # a = a + dt.timedelta(minutes=1)
    
    
  
# # # response = HttpResponse(content_type='text/csv')  
# # # response['Content-Disposition'] = 'attachment; filename="oura_intraday'+oura_dates[-1]+'.csv"'  
# # # writer = csv.writer(response)
# # # writer.writerow(["Time",  "HeartRate", "Date:"+ oura_dates[-1]])
# # # for i in range(len(oura_hr_times)):
    # # # writer.writerow([oura_hr_times[i], oura_hr_intraday[i]])  
# # # writer.writerow([])
# # # writer.writerow(["Time", "MET", "Date:"+ oura_dates[-1]])
# # # for i in range(len(oura_met_times)):
    # # # writer.writerow([oura_met_times[i], oura_met_intraday[i]])  
# # # return response

# ## https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https%3A%2F%2Fappomics.org%2Flogin%2Fredirectapp&prompt=consent&response_type=code&client_id=247905637458-20ucdqrb0vrktd0jdupot67hto9ar0ln.apps.googleusercontent.com&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.activity.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.blood_glucose.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.blood_pressure.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.body.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.body_temperature.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.heart_rate.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.location.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.nutrition.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.oxygen_saturation.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.reproductive_health.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.sleep.read&access_type=offline&flowName=GeneralOAuthFlow

