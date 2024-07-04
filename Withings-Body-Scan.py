import requests
import json
import csv
import datetime as dt
import os
import time
import pytz
from datetime import datetime

# Define the Withings API token endpoint and your credentials
token_url = 'https://wbsapi.withings.net/v2/oauth2'
client_id = "**************Put--your-client-id**************"
client_secret = "**************Put--your-client-secret**************"

GetUser_url = "**************Your-get-details-id**************"
PatchDynamoDB_url = "****************--your-AWS-fetching-api-id**************"

# Define the parameters for the GetUser request
userData = {
    "ID": "**************Put--your-client-id**************"
}

user_response = requests.post(GetUser_url, json=userData).json()
print(user_response)
refresh_token = user_response["RefreshToken"]

# Define the parameters for the token request
payload = {
    "action": "requesttoken",
    "grant_type": "refresh_token",
    "client_id": client_id,
    "client_secret": client_secret,
    "refresh_token": refresh_token,
}

r_token = requests.post(token_url, data=payload).json()
Withings_access_token = r_token['body']["access_token"]
Withings_refresh_token = r_token['body']["refresh_token"]
print("Withings_access_token:", Withings_access_token)
print("Withings_refresh_token:", Withings_refresh_token)

# Payload for Save Request
if len(Withings_refresh_token) == 0:
    print("No Refresh token")
else:
    api_data = {
        "Phone": user_response["Phone"],
        "Timestamp": user_response["Timestamp"],
        "Gender": user_response["Gender"],
        "WearableType": user_response["WearableType"],
        "FirstName": user_response["FirstName"],
        "ID": user_response["ID"],
        "LastName": user_response["LastName"],
        "Email": user_response["Email"],
        "RefreshToken": Withings_refresh_token,
        "Age": user_response["Age"]
    }

# Make the POST request to save the refresh token back to DB
api_response = requests.patch(PatchDynamoDB_url, json=api_data)
print("Response Content:", api_response.text)

# Withings Data Fetch
from datetime import date

current_Date = dt.date.today()
Previous_Date = date(2024, 5,31) #change to end date
delta = current_Date - Previous_Date
print(delta.days)

# Loop through the days
for i in range(delta.days, delta.days + 31):
    date = str(dt.date.today() - dt.timedelta(days=i))

    start = dt.datetime.combine(dt.date.today(), dt.datetime.min.time()) - dt.timedelta(days=i)
    start_unix = int(start.timestamp())

    end = dt.datetime.combine(dt.date.today(), dt.datetime.min.time()) - dt.timedelta(days=i - 1)
    end_unix = int(end.timestamp())

    header = {
        'Content-type': 'application/json',
        'Authorization': 'Bearer ' + Withings_access_token
    }

    # HEARTRATE DATA FETCH
    payload = {
        "action": "getmeas", 
        #"meastypes": "77,168,169", 
        "meastypes": "1,4,5,6,8,9,10,11,12,54,71,73,76,77,88,91,123,130,135,136,137,138,139,155,158,159,167,168,169,170,174,175,196,197,198", 
        "category": 1,
        "startdate": start_unix, 
        "enddate": end_unix, 
        "offset": 0
    }

    r_token = requests.post('https://wbsapi.withings.net/measure', headers=header, data=payload).json()
    print(r_token)

    data = [
    {'Value': 1, 'Description': 'Weight (kg)'},
    {'Value': 4, 'Description': 'Height (meter)'},
    {'Value': 5, 'Description': 'Fat Free Mass (kg)'},
    {'Value': 6, 'Description': 'Fat Ratio (%)'},
    {'Value': 8, 'Description': 'Fat Mass Weight (kg)'},
    {'Value': 9, 'Description': 'Diastolic Blood Pressure (mmHg)'},
    {'Value': 10, 'Description': 'Systolic Blood Pressure (mmHg)'},
    {'Value': 11, 'Description': 'Heart Pulse (bpm) - only for BPM and scale devices'},
    {'Value': 12, 'Description': 'Temperature (celsius)'},
    {'Value': 54, 'Description': 'SP02 (%)'},
    {'Value': 71, 'Description': 'Body Temperature (celsius)'},
    {'Value': 73, 'Description': 'Skin Temperature (celsius)'},
    {'Value': 76, 'Description': 'Muscle Mass (kg)'},
    {'Value': 77, 'Description': 'Hydration (kg)'},
    {'Value': 88, 'Description': 'Bone Mass (kg)'},
    {'Value': 91, 'Description': 'Pulse Wave Velocity (m/s)'},
    {'Value': 123, 'Description': 'VO2 max is a numerical measurement of your body’s ability to consume oxygen (ml/min/kg)'},
    {'Value': 130, 'Description': 'Atrial fibrillation result'},
    {'Value': 135, 'Description': 'QRS interval duration based on ECG signal'},
    {'Value': 136, 'Description': 'PR interval duration based on ECG signal'},
    {'Value': 137, 'Description': 'QT interval duration based on ECG signal'},
    {'Value': 138, 'Description': 'Corrected QT interval duration based on ECG signal'},
    {'Value': 139, 'Description': 'Atrial fibrillation result from PPG'},
    {'Value': 155, 'Description': 'Vascular age'},
    {'Value': 158, 'Description': 'Nerve Health Score Conductance 3 electrodes Left Foot'},
    {'Value': 159, 'Description': 'Nerve Health Score Conductance 3 electrodes Right Foot'},
    {'Value': 167, 'Description': 'Nerve Health Score Conductance 2 electrodes Feet'},
    {'Value': 168, 'Description': 'Extracellular Water in kg'},
    {'Value': 169, 'Description': 'Intracellular Water in kg'},
    {'Value': 170, 'Description': 'Visceral Fat (without unity)'},
    {'Value': 174, 'Description': 'Fat Mass for segments in mass unit'},
    {'Value': 175, 'Description': 'Muscle Mass for segments'},
    {'Value': 196, 'Description': 'Electrodermal activity feet'},
    {'Value': 197, 'Description': 'Electrodermal activity left foot'},
    {'Value': 198, 'Description': 'Electrodermal activity right foot'}
    ]
    # Create a dictionary for easy lookup
    data_dict = {item['Value']: item['Description'] for item in data}

    withings_dates = []
    withings_type = []
    withings_value = []
    withings_position = []
    withings_unit = []

    # Define the Chicago time zone
    chicago_timezone = pytz.timezone('America/Chicago')

    for measuregrp in r_token['body']['measuregrps']:
        timestamp = int(measuregrp['date'])
        # Extract the UTC timestamp from the 'created' field
        utc_timestamp = datetime.fromtimestamp(timestamp, tz=pytz.UTC)

        # Define the Chicago time zone
        chicago_timezone = pytz.timezone('America/Chicago')

        # Convert the UTC timestamp to Chicago time
        withings_date = utc_timestamp.astimezone(chicago_timezone)

        print("UTC Timestamp:", utc_timestamp)
        print("Chicago Timestamp:", withings_date)
        
        model_device = measuregrp['model']
        for measure in measuregrp['measures']:
            measure_type = measure['type']
            measure_value = measure['value']
            measure_unit = measure['unit']
            withings_dates.append(withings_date)
            withings_type.append(measure_type)
            withings_value.append(measure_value)
            withings_unit.append(measure_unit)
            if 'position' in measure:
                position_value = measure['position']
                withings_position.append(position_value)
            else:
                withings_position.append(0)    
            print(f"Type: {measure_type}, Value: {measure_value}, unit: {measure_unit}")
    

    # Save data to a CSV file with a dynamic filename based on the date
    csv_filename = f"D:/Pavan/Withings/Data/Bodyscan/May/V1__bodyscan_{date}.csv"
    #csv_filename = f"D:/Pavan/Withings/Data/Hydration/V1__bodyscan_{date}.csv"
    os.makedirs(os.path.dirname(csv_filename), exist_ok=True)

    with open(csv_filename, 'w') as csvfile:
        writer = csv.writer(csvfile, lineterminator='\n')
        writer.writerow(["VolunteerID","V1"])
        writer.writerow(["Date", date])
      # writer.writerow(["Device Model", model_device])
     #  writer.writerow(["Datatype", "Type","Description" "Value","Position"])
        writer.writerow(["","", "", "",""])
        writer.writerow(["DateTime","Type","Description" ,"Value","Position"])
        for i in range(len(withings_type)):
            if i < len(withings_type) and withings_type[i] != 0:
                description = data_dict.get(withings_type[i])
                writer.writerow( [withings_dates[i],withings_type[i],description, (withings_value[i]* 10 ** (withings_unit[i])),withings_position[i]])


