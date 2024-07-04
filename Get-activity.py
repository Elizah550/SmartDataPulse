import requests
import json
import csv
import datetime as dt
import os
import time
from datetime import datetime
import openpyxl
from openpyxl import Workbook

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
print(r_token)
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
    print(api_data)

# Make the POST request to save the refresh token back to DB
api_response = requests.patch(PatchDynamoDB_url, json=api_data)
print(api_response)
print("Response Content:", api_response.text)

# Withings Data Fetch
from datetime import date

current_Date = dt.date.today()
Previous_Date = date(2023, 10, 1)
delta = current_Date - Previous_Date
print(delta.days)



# Loop through the days
for i in range(delta.days, delta.days +3):
    date = str(dt.date.today() - dt.timedelta(days=i))

    start = dt.datetime.combine(dt.date.today(), dt.datetime.min.time()) - dt.timedelta(days=i)
    start_unix_timestamp = int(start.timestamp())  # Convert to Unix timestamp


    end = dt.datetime.combine(dt.date.today(), dt.datetime.min.time()) - dt.timedelta(days=i - 1)
   
    end_unix_timestamp = int(end.timestamp())  # Convert to Unix timestamp
    
    header = {
    'Content-type': 'application/json',
    'Authorization': 'Bearer ' + Withings_access_token
}

# HEARTRATE DATA FETCH
payload = {
    "action": "getactivity",
    "startdateymd": '2024-06-01',  # Ensure leading zeros for months and days if necessary
    "enddateymd": '2024-06-03',
    "data_fields": "steps,distance,calories,totalcalories,hr_average,hr_min,hr_max,hr_zone_0,hr_zone_1,hr_zone_2,hr_zone_3"
}
    

data = requests.post('https://wbsapi.withings.net/v2/measure', headers=header, data=payload).json()
print(data)

# Function to save the extracted data to an Excel file
def save_to_excel(data, user_response, Withings_access_token, date):
    activities = data['body']['activities']

    # Create a new workbook and select the active worksheet
    wb = Workbook()
    ws = wb.active

    # Write the user details
    ws.append(["Firstame", user_response["FirstName"]])
    ws.append(["Lastame", user_response["LastName"]])
    ws.append(["Phone", user_response["Phone"]])
    ws.append(["Email", user_response["Email"]])
    ws.append(["Token", Withings_access_token])
    ws.append(["Date", date])
    ws.append(["Datatype", "GetActivity"])
    ws.append(["", ""])
    ws.append(["date", "steps","distance","calories","totalcalories","hr_average","hr_min","hr_max","hr_zone_0","hr_zone_1","hr_zone_2","hr_zone_3"])

    # Write the activities data
    for activity in activities:
        row = [
            activity['date'],
            activity['steps'],
            activity['distance'],
            activity['calories'],
            activity['totalcalories'],
            activity['hr_average'],
            activity['hr_min'],
            activity['hr_max'],
            activity['hr_zone_0'],
            activity['hr_zone_1'],
            activity['hr_zone_2'],
            activity['hr_zone_3']
        ]
        ws.append(row)

    # Save the workbook
    filename = f"D://Pavan/{user_response['FirstName']}{user_response['LastName']}__getactivity_{date}.xlsx"
    wb.save(filename)
save_to_excel(data, user_response, Withings_access_token, date)


