from django.shortcuts import render, redirect
import requests
import json
from django.contrib.auth.decorators import login_required
from django.contrib import auth
import os
import boto3
from boto3.dynamodb.conditions import Key
from django.contrib.auth.models import User
import pandas as pd
import datetime as dt
from django.views.generic import View
from django.http import JsonResponse
import csv
from django.http import HttpResponse
from zipfile import ZipFile
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt        
def gateway_post(request):
    if request.method == "POST":
        #try:
            #table = dynamodb.Table('GatewayTest')
            #table.put_item(
            #Item={
            #        "data":str(request.body),
            #})
            #r = requests.post('https://fcr56uaai7.execute-api.ap-south-1.amazonaws.com/Test/gatewaypost', data={'body': request.body})
            print(str(request.body))
            return HttpResponse("00", content_type="text/plain")
        #except:
           # return HttpResponse("01", content_type="text/plain")


def myappleunilink(request):
    data = {
        "applinks": {
            "apps": [],
            "details": [
                {
                    "appID": "W8567BN85F.org.curescience.otp",
                    "paths": [ "*" ]
                },
            ]
        }
    }
    return JsonResponse(data)


def cure_trial(request):
    context = {}
    if request.method == 'POST':
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        request.session["website"] = "Original"
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        wearable = request.POST.get("wearable")

        request.session["firstname"] = firstname
        request.session["lastname"] = lastname
        request.session["email"] = email
        request.session["phone"] = phone
        print(firstname, lastname, wearable)

        if wearable == "Fitbit":
            return redirect("https://www.fitbit.com/oauth2/authorize?response_type=token&client_id=23BCNB&redirect_uri=https://cure.science/login/redirectapp&scope=activity%20nutrition%20heartrate%20location%20nutrition%20profile%20settings%20sleep%20social%20weight&expires_in=31536000")
        elif wearable == "OuraRing":
            return redirect("https://cloud.ouraring.com/oauth/authorize?response_type=token&client_id=MWGRDU6WOIVNP4A6&redirect_uri=https://cure.science/login/redirectapp&scope=email+personal+daily&state=MZJMwJIqPLdQ3I69z5zIFNuD99YJcm")
        elif wearable == "GoogleFit":
            return redirect("https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https://cure.science/login/redirectapp&prompt=consent&response_type=code&client_id=97768613938-7bhmm950g166dhkqg8kpk57ofcrm8cqn.apps.googleusercontent.com&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.activity.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.activity.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.blood_glucose.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.blood_glucose.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.blood_pressure.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.blood_pressure.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.body.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.body.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.body_temperature.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.body_temperature.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.heart_rate.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.heart_rate.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.location.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.location.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.nutrition.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.nutrition.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.oxygen_saturation.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.oxygen_saturation.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.reproductive_health.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.reproductive_health.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.sleep.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.sleep.write&access_type=offline&flowName=GeneralOAuthFlow")

  
    return render(request,'homepage/cure_trial.html', context)

def cure_test_trial(request):
    context = {}
    if request.method == 'POST':
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        wearable = request.POST.get("wearable")

        request.session["firstname"] = firstname
        request.session["lastname"] = lastname
        request.session["email"] = email
        request.session["phone"] = phone
        print("################################")
        print(firstname, lastname, wearable)

        if wearable == "Fitbit":
            return redirect("https://www.fitbit.com/oauth2/authorize?response_type=token&client_id=23BCNB&redirect_uri=https://cure.science/login/redirectapp&scope=activity%20nutrition%20heartrate%20location%20nutrition%20profile%20settings%20sleep%20social%20weight&expires_in=31536000")
        elif wearable == "OuraRing":
            return redirect("https://cloud.ouraring.com/oauth/authorize?response_type=token&client_id=MWGRDU6WOIVNP4A6&redirect_uri=https://cure.science/login/redirectapp&scope=email+personal+daily&state=MZJMwJIqPLdQ3I69z5zIFNuD99YJcm")
        elif wearable == "GoogleFit":
            return redirect("https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https://cure.science/login/redirectapp&prompt=consent&response_type=code&client_id=97768613938-7bhmm950g166dhkqg8kpk57ofcrm8cqn.apps.googleusercontent.com&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.activity.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.activity.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.blood_glucose.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.blood_glucose.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.blood_pressure.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.blood_pressure.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.body.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.body.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.body_temperature.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.body_temperature.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.heart_rate.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.heart_rate.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.location.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.location.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.nutrition.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.nutrition.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.oxygen_saturation.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.oxygen_saturation.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.reproductive_health.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.reproductive_health.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.sleep.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.sleep.write&access_type=offline&flowName=GeneralOAuthFlow")
        elif wearable == "Withings":
            #return redirect("https://account.withings.com/oauth2_user/authorize2?response_type=code&client_id=efaac2aec0998bc837ba2a0edd121332bf49606f8828ef383ef699ddd708e9ba&redirect_uri=https%3A%2F%2Fcure.science%2Flogin%2FredirectGHP&state=dk6f30bN7XKmHSt&scope=user.metrics%2Cuser.activity")
            return redirect("https://account.withings.com/oauth2_user/authorize2?response_type=code&client_id=87d5689ceb6568d2e2fd6dc45ab243cf518d126132eb1b851f36dda3dc8ee4bc&redirect_uri=https%3A%2F%2Fcure.science%2Flogin%2FredirectGHP&state=dk6f30bN7XKmHSt&scope=user.metrics%2Cuser.activity")
        elif wearable == "Samsung":
            return redirect("https://graph.api.smartthings.com/oauth/authorize?response_type=code&client_id=CLIENT_ID&scope=app&redirect_uri=https://cure.science/login/redirectapp%2Foauth%2Fcallback")  
    return render(request,'homepage/cure_test_trial.html', context)

#Wearables GHP
def GHP_Wearables(request):
    context = {}
    if request.method == 'POST':
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        wearable = request.POST.get("wearable")

        request.session["firstname"] = firstname
        request.session["website"] = "GHPWearables"
        request.session["lastname"] = lastname
        request.session["email"] = email
        request.session["phone"] = phone
        print(firstname, lastname, wearable)

        if wearable == "Fitbit":
            return redirect("https://www.fitbit.com/oauth2/authorize?response_type=token&client_id=23BCNB&redirect_uri=https://cure.science/login/redirectapp&scope=activity%20nutrition%20heartrate%20location%20nutrition%20profile%20settings%20sleep%20social%20weight&expires_in=31536000")
        elif wearable == "OuraRing":
            return redirect("https://cloud.ouraring.com/oauth/authorize?response_type=token&client_id=MWGRDU6WOIVNP4A6&redirect_uri=https://cure.science/login/redirectapp&scope=email+personal+daily&state=MZJMwJIqPLdQ3I69z5zIFNuD99YJcm")
        elif wearable == "GoogleFit":
            return redirect("https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https://cure.science/login/redirectapp&prompt=consent&response_type=code&client_id=97768613938-7bhmm950g166dhkqg8kpk57ofcrm8cqn.apps.googleusercontent.com&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.activity.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.activity.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.blood_glucose.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.blood_glucose.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.blood_pressure.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.blood_pressure.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.body.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.body.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.body_temperature.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.body_temperature.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.heart_rate.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.heart_rate.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.location.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.location.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.nutrition.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.nutrition.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.oxygen_saturation.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.oxygen_saturation.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.reproductive_health.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.reproductive_health.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.sleep.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.sleep.write&access_type=offline&flowName=GeneralOAuthFlow")
        elif wearable == "MI Band":
            return redirect("https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https://cure.science/login/redirectapp&prompt=consent&response_type=code&client_id=97768613938-7bhmm950g166dhkqg8kpk57ofcrm8cqn.apps.googleusercontent.com&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.activity.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.activity.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.blood_glucose.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.blood_glucose.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.blood_pressure.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.blood_pressure.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.body.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.body.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.body_temperature.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.body_temperature.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.heart_rate.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.heart_rate.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.location.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.location.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.nutrition.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.nutrition.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.oxygen_saturation.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.oxygen_saturation.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.reproductive_health.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.reproductive_health.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.sleep.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.sleep.write&access_type=offline&flowName=GeneralOAuthFlow")
        elif wearable == "Withings":
            return redirect("https://account.withings.com/oauth2_user/authorize2?response_type=code&client_id=87d5689ceb6568d2e2fd6dc45ab243cf518d126132eb1b851f36dda3dc8ee4bc&redirect_uri=https%3A%2F%2Fcure.science%2Flogin%2FredirectGHP&state=dk6f30bN7XKmHSt&scope=user.metrics%2Cuser.activity")
        elif wearable == "Samsung":
            return redirect("https://graph.api.smartthings.com/oauth/authorize?response_type=code&client_id=CLIENT_ID&scope=app&redirect_uri=https://cure.science/login/redirectapp%2Foauth%2Fcallback")
    return render(request,'homepage/GHP_Wearables.html', context)

####
#Wearables GHP
def Wearables(request):
    context = {}
    if request.method == 'POST':
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        wearable = request.POST.get("wearable")

        request.session["firstname"] = firstname
        request.session["website"] = "Wearables"
        request.session["lastname"] = lastname
        request.session["email"] = email
        request.session["phone"] = phone
        print(firstname, lastname, wearable)

        if wearable == "Fitbit":
            return redirect("https://www.fitbit.com/oauth2/authorize?response_type=token&client_id=23BCNB&redirect_uri=https://cure.science/login/redirectapp&scope=activity%20nutrition%20heartrate%20location%20nutrition%20profile%20settings%20sleep%20social%20weight&expires_in=31536000")
        elif wearable == "OuraRing":
            return redirect("https://cloud.ouraring.com/oauth/authorize?response_type=token&client_id=MWGRDU6WOIVNP4A6&redirect_uri=https://cure.science/login/redirectapp&scope=email+personal+daily&state=MZJMwJIqPLdQ3I69z5zIFNuD99YJcm")
        elif wearable == "GoogleFit":
            return redirect("https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https://cure.science/login/redirectapp&prompt=consent&response_type=code&client_id=97768613938-7bhmm950g166dhkqg8kpk57ofcrm8cqn.apps.googleusercontent.com&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.activity.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.activity.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.blood_glucose.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.blood_glucose.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.blood_pressure.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.blood_pressure.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.body.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.body.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.body_temperature.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.body_temperature.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.heart_rate.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.heart_rate.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.location.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.location.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.nutrition.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.nutrition.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.oxygen_saturation.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.oxygen_saturation.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.reproductive_health.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.reproductive_health.write%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.sleep.read%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.sleep.write&access_type=offline&flowName=GeneralOAuthFlow")
        elif wearable == "Withings":
            return redirect("https://account.withings.com/oauth2_user/authorize2?response_type=code&client_id=efaac2aec0998bc837ba2a0edd121332bf49606f8828ef383ef699ddd708e9ba&redirect_uri=https%3A%2F%2Fcure.science%2Flogin%2FredirectGHP&state=dk6f30bN7XKmHSt&scope=user.metrics%2Cuser.activity")
  
    return render(request,'homepage/Wearables.html', context)

####

def toc(request):
    return render(request,'homepage/Terms&Conditions.html')

def privacy(request):
    return render(request,'homepage/privacy.html')

def privacyweb(request):
    return render(request,'homepage/privacyweb.html')


def wearables(request):
    context = {}
    return render(request,'homepage/wearables.html', context) 

@login_required(login_url="loginadmin")
def csvdownloader(request):
    dynamodb= boto3.resource('dynamodb',region_name='ap-south-1',aws_access_key_id='xxxxxxx',aws_secret_access_key='xxxxxxxxx')
    tableuser = dynamodb.Table('cure_trial')
    response = tableuser.scan()    
    items = response['Items']

    context = {
        "items" : items,
        }
    return render(request,'homepage/datadownload.html',context)

@login_required(login_url="loginadmin")
def csvcreator(request):
    if request.method == "POST":
        # print(request.POST.get("user"))
        # print(request.POST.get("datatype"))
        # print(request.POST.get("startdate"))
        # print(request.POST.get("enddate"))
        print(request.POST.get("daterange"))
        daterange = request.POST.get("daterange")

        dates = daterange.split()
        print(dates)

        startdate = dates[0]
        enddate = dates[-1]
        print(request.POST.get("heartrate"))
        print(request.POST.get("stecalele"))
        print(request.POST.get("sleep"))

        if request.POST.get("wearable") == "fitbit":
            username = request.POST.get("user")
    
            dynamodb= boto3.resource('dynamodb',region_name='ap-south-1',aws_access_key_id='xxxxxxxxxxxxxxx',aws_secret_access_key='xxxxxxxxxxxxxxxxxxxx')
            if username == "Weekly":      
                tableuser = dynamodb.Table('cure_trial')
                response = tableuser.scan()    
                items = response['Items']

                zipObj = ZipFile('sample.zip', 'w')
                for item in items:
                    username = item["name"]+item["phone"]

                    zipObj.write("fitbit_data/"+ username +"/"+ username +"patientinfo.txt")
                    zipObj.write("fitbit_data/"+ username +"/"+ username +"user_profile.csv")
                    today = dt.date.today()

                    for i in range(2,9):
                        date = str(today-dt.timedelta(days = i))
                        try:
                            zipObj.write("fitbit_data/"+username+"/"+ username +"intraday_heartrate_"+date+".csv")
                            zipObj.write("fitbit_data/"+username+"/"+ username +"heartrate_summary_"+date+".csv")
                        except:
                            None
                        try:
                            zipObj.write("fitbit_data/"+username+"/"+ username +"intraday_steps_cal_elev_"+date+".csv")
                            zipObj.write("fitbit_data/"+username+"/"+ username +"activity_summary_"+date+".csv")
                        except:
                            None 
                        try:
                            zipObj.write("fitbit_data/"+username+"/"+ username +"intraday_sleep_"+date+".csv")
                        except:
                            None
                zipObj.close()
                
                file = open("sample.zip", "rb")
                response = HttpResponse(file, content_type='application/zip')  
                response['Content-Disposition'] = 'attachment; filename="fitbit_Weekly'+"_"+startdate+"to"+enddate+'.zip"'

                
                
                os.remove("sample.zip")

                return response

            today = dt.date.today()
            date = str(today - dt.timedelta(days = 8))
            today = dt.datetime.strptime(startdate, "%m/%d/%Y").date()
            nextday = dt.datetime.strptime(enddate, "%m/%d/%Y").date()
            delta = nextday - today
            print(today + dt.timedelta(days = delta.days))
            date=startdate

            zipObj = ZipFile('sample.zip', 'w')

            zipObj.write("fitbit_data/"+ username +"/"+ username +"patientinfo.txt")
            zipObj.write("fitbit_data/"+ username +"/"+ username +"user_profile.csv")
            #########################################HEART RATE
            if request.POST.get("heartrate") == "on":

                for i in range(delta.days+1):

                    date = str(today + dt.timedelta(days = i))

                    # dates=[]
                    # values=[]

                    

                    # response = requests.get("https://api.fitbit.com/1/user/-/activities/heart/date/"+date+"/1d/1sec.json", headers=header).json()
                    # steps_intraday = response['activities-heart-intraday']['dataset']
                    
                    # try:
                    #     for line in steps_intraday:
                    #         dates.append(line['time'][0:8])
                    #         values.append(line['value'])
                            
                    #     with open("intraday_heartrate_"+date+".csv", 'w') as csvfile:
                    #         writer = csv.writer(csvfile, lineterminator = '\n')
                    #         writer.writerow(["Time", "HeartRate"])
                    #         for i in range(len(dates)):
                    #             writer.writerow([dates[i], values[i]])

                    #     zipObj.write("intraday_heartrate_"+date+".csv")
                    #     os.remove("intraday_heartrate_"+date+".csv")
                    # except:
                    #     None

                    try:
                        zipObj.write("fitbit_data/"+username+"/"+ username +"intraday_heartrate_"+date+".csv")
                        zipObj.write("fitbit_data/"+username+"/"+ username +"heartrate_summary_"+date+".csv")
                    except:
                        None

            ####################################### SCE

            if request.POST.get("stecalele") == "on":

                for i in range(delta.days+1):

                    date = str(today + dt.timedelta(days = i))

                    # dates = []
                    # steps_values = []
                    # calories_values = []
                    # elevation_values = []

                    # response = requests.get("https://api.fitbit.com/1/user/-/activities/steps/date/"+date+"/1d/1min.json", headers=header).json()
                    # steps_intraday = response['activities-steps-intraday']['dataset']

                    # try:
                    #     for line in steps_intraday:
                    #         dates.append(line['time'][0:5])
                    #         steps_values.append(line['value'])
                            
                    #     response = requests.get("https://api.fitbit.com/1/user/-/activities/calories/date/"+date+"/1d/1min.json", headers=header).json()
                    #     steps_intraday = response['activities-calories-intraday']['dataset']
                    #     for line in steps_intraday:
                    #         calories_values.append(line['value'])
                            
                    #     response = requests.get("https://api.fitbit.com/1/user/-/activities/elevation/date/"+date+"/1d/1min.json", headers=header).json()
                    #     steps_intraday = response['activities-elevation-intraday']['dataset']
                    #     for line in steps_intraday:
                    #         elevation_values.append(int(line['value'])*10)

                    #     with open("intraday_steps_cal_elev_"+date+".csv", 'w') as csvfile:
                    #         writer = csv.writer(csvfile, lineterminator = '\n')
                    #         writer.writerow(["Time", "Steps", "Calories Burnt", "Elevation (m)"])
                    #         for i in range(len(dates)):
                    #             writer.writerow([dates[i], steps_values[i], calories_values[i], elevation_values[i]])

                    #     zipObj.write("intraday_steps_cal_elev_"+date+".csv")
                    #     os.remove("intraday_steps_cal_elev_"+date+".csv")
                    # except:
                    #     None

                    try:
                        zipObj.write("fitbit_data/"+username+"/"+ username +"intraday_steps_cal_elev_"+date+".csv")
                        zipObj.write("fitbit_data/"+username+"/"+ username +"activity_summary_"+date+".csv")
                    except:
                        None 

            #3#################################### SLEEEP

            if request.POST.get("sleep") == "on":

                for i in range(delta.days+1):

                    date = str(today + dt.timedelta(days = i))
                    # response = requests.get("https://api.fitbit.com/1.2/user/-/sleep/date/"+date+".json", headers=header).json()
                    
                    # steps = response['sleep']

                    

                    # dates = []
                    # values = []
                    # sleep_levels = []

                    # try:
                    #     intra = steps[0]['levels']['data']
                    #     for line in intra:
                    #         dates.append(line['dateTime'])
                    #         values.append(int(int(line['seconds'])/60))
                    #         sleep_levels.append(line['level'])  

                    #     with open("intraday_sleep_"+date+".csv", 'w') as csvfile:
                    #         writer = csv.writer(csvfile, lineterminator = '\n')
                    #         writer.writerow(["Timestamp", "Minutes Asleep", "Sleep Type"])
                    #         for i in range(len(dates)):
                    #             writer.writerow([dates[i], values[i], sleep_levels[i]])

                    #     zipObj.write("intraday_sleep_"+date+".csv")
                    #     os.remove("intraday_sleep_"+date+".csv")
                    # except:
                    #     None

                    try:
                        zipObj.write("fitbit_data/"+username+"/"+ username +"intraday_sleep_"+date+".csv")
                    except:
                        None 


            
            # Add multiple files to the zip
         
            # close the Zip File
            zipObj.close()
            
            file = open("sample.zip", "rb")
            response = HttpResponse(file, content_type='application/zip')  
            response['Content-Disposition'] = 'attachment; filename="fitbit_'+username+"_"+startdate+"to"+enddate+'.zip"'

            
            
            os.remove("sample.zip")

            return response


        elif request.POST.get("wearable") == "oura":

            username = request.POST.get("user")
    
            dynamodb= boto3.resource('dynamodb',region_name='ap-south-1',aws_access_key_id='xxxxxxxx',aws_secret_access_key='xxxxxxxxxxxxx')
            tableuser = dynamodb.Table('Userdetails')
            scan_kwargs = {
                    'FilterExpression': Key('username').eq(username)
                }
            response = tableuser.scan(
                    **scan_kwargs
                )
            items = response['Items'][0]
            
            tablefitbit = dynamodb.Table('ouraring')
            scan_kwargs = {
                    'FilterExpression': Key('userphone').eq(items["phone"])
                }
            response = tablefitbit.scan(
                    **scan_kwargs
                )
            item = response['Items'][0]

            print(item)
            access_token = "access_token=" + item['token']

            # startdate = request.POST.get("startdate")
            # enddate = request.POST.get("enddate")

           
        
            # # access_token = "access_token=" + "6G3PP2NJYBX3DDYNKEQXT4JJESF6OOGL"
            
            # today = dt.date.today()
            # previous = today - dt.timedelta(days = 30)

            # response = requests.get("https://api.ouraring.com/v1/sleep?start="+str(startdate)+"&end="+str(enddate)+"&"+access_token).json()
            # print(response)
            # while len(response['sleep']) == 0:
            #     previous = previous - dt.timedelta(days = 1)
            #     response = requests.get("https://api.ouraring.com/v1/sleep?start="+str(previous)+"&end="+str(today)+"&"+access_token).json()

            # oura_dates = []
            # oura_values = []
            # oura_hr_values = []
            # oura_hr_intraday = []
            # oura_hr_starttime = ""
            # oura_hr_times = []
            # for item in response['sleep']:
            #     oura_dates.append(item['bedtime_end'][0:10])
            #     oura_values.append(int(int(item['duration'])/60))
            #     oura_hr_values.append(item['hr_average'])
            #     oura_hr_intraday = item['hr_5min']
            #     oura_hr_starttime = item['bedtime_start']
            
            # a = dt.datetime.now()    
            # hr = oura_hr_starttime[11:13]
            # sc = oura_hr_starttime[14:16]
            # a = a.replace(hour=int(hr),minute=int(sc),second=0)
            # for ab in range(len(oura_hr_intraday)):
            #     oura_hr_times.append(str(a)[11:16])
            #     a = a + dt.timedelta(minutes=5)

            # previous = today - dt.timedelta(days = 30)

            # response2 = requests.get("https://api.ouraring.com/v1/activity?start="+str(startdate)+"&end="+str(enddate)+"&"+access_token).json()
            # while len(response2['activity']) == 0:
            #     previous = previous - dt.timedelta(days = 1)
            #     response2 = requests.get("https://api.ouraring.com/v1/activity?start="+str(previous)+"&end="+str(today)+"&"+access_token).json()

            # oura_dates2 = []
            # oura_steps_values = []
            # oura_calories_values = []
            # oura_met_values = []
            # oura_met_intraday = []
            # oura_met_times = []
            # for item in response2['activity']:
            #     oura_dates2.append(item['summary_date'])
            #     oura_steps_values.append(item['steps'])
            #     oura_calories_values.append(item["cal_total"])
            #     oura_met_values.append(item['average_met'])
            #     oura_met_intraday = item["met_1min"]

            # a = dt.datetime.now()    
            # hr = "04"
            # sc = "00"
            # a = a.replace(hour=int(hr),minute=int(sc),second=0)
            # for ab in range(len(oura_met_intraday)):
            #     oura_met_times.append(str(a)[11:16])
            #     a = a + dt.timedelta(minutes=1)
            # response = HttpResponse(content_type='text/csv')  
            # response['Content-Disposition'] = 'attachment; filename="oura_intraday'+oura_dates[-1]+'.csv"'  
            # writer = csv.writer(response)
            # writer.writerow(["Time",  "HeartRate", "Date:"+ oura_dates[-1]])
            # for i in range(len(oura_hr_times)):
            #     writer.writerow([oura_hr_times[i], oura_hr_intraday[i]])  
            # writer.writerow([])
            # writer.writerow(["Time", "MET", "Date:"+ oura_dates[-1]])
            # for i in range(len(oura_met_times)):
            #     writer.writerow([oura_met_times[i], oura_met_intraday[i]])  
            # return response

            today = dt.datetime.strptime(startdate, "%m/%d/%Y").date()
            nextday = dt.datetime.strptime(enddate, "%m/%d/%Y").date()
            delta = nextday - today
            print(today + dt.timedelta(days = delta.days))
            date=startdate

            zipObj = ZipFile('sample.zip', 'w')
            #########################################HEART RATE
            if request.POST.get("heartrate") == "on":

                for i in range(delta.days+1):

                    date = str(today + dt.timedelta(days = i))

                    # dates=[]
                    # values=[]

                    

                    # response = requests.get("https://api.fitbit.com/1/user/-/activities/heart/date/"+date+"/1d/1sec.json", headers=header).json()
                    # steps_intraday = response['activities-heart-intraday']['dataset']
                    
                    # try:
                    #     for line in steps_intraday:
                    #         dates.append(line['time'][0:8])
                    #         values.append(line['value'])
                            
                    #     with open("intraday_heartrate_"+date+".csv", 'w') as csvfile:
                    #         writer = csv.writer(csvfile, lineterminator = '\n')
                    #         writer.writerow(["Time", "HeartRate"])
                    #         for i in range(len(dates)):
                    #             writer.writerow([dates[i], values[i]])

                    #     zipObj.write("intraday_heartrate_"+date+".csv")
                    #     os.remove("intraday_heartrate_"+date+".csv")
                    # except:
                    #     None

                    try:
                        zipObj.write("oura_data\sleep_heartrate_"+date+".csv")
                    except:
                        None

            ####################################### SCE

            if request.POST.get("stecalele") == "on":

                for i in range(delta.days+1):

                    date = str(today + dt.timedelta(days = i))

                    # dates = []
                    # steps_values = []
                    # calories_values = []
                    # elevation_values = []

                    # response = requests.get("https://api.fitbit.com/1/user/-/activities/steps/date/"+date+"/1d/1min.json", headers=header).json()
                    # steps_intraday = response['activities-steps-intraday']['dataset']

                    # try:
                    #     for line in steps_intraday:
                    #         dates.append(line['time'][0:5])
                    #         steps_values.append(line['value'])
                            
                    #     response = requests.get("https://api.fitbit.com/1/user/-/activities/calories/date/"+date+"/1d/1min.json", headers=header).json()
                    #     steps_intraday = response['activities-calories-intraday']['dataset']
                    #     for line in steps_intraday:
                    #         calories_values.append(line['value'])
                            
                    #     response = requests.get("https://api.fitbit.com/1/user/-/activities/elevation/date/"+date+"/1d/1min.json", headers=header).json()
                    #     steps_intraday = response['activities-elevation-intraday']['dataset']
                    #     for line in steps_intraday:
                    #         elevation_values.append(int(line['value'])*10)

                    #     with open("intraday_steps_cal_elev_"+date+".csv", 'w') as csvfile:
                    #         writer = csv.writer(csvfile, lineterminator = '\n')
                    #         writer.writerow(["Time", "Steps", "Calories Burnt", "Elevation (m)"])
                    #         for i in range(len(dates)):
                    #             writer.writerow([dates[i], steps_values[i], calories_values[i], elevation_values[i]])

                    #     zipObj.write("intraday_steps_cal_elev_"+date+".csv")
                    #     os.remove("intraday_steps_cal_elev_"+date+".csv")
                    # except:
                    #     None

                    try:
                        
                        zipObj.write("oura_data\intraday_met_"+date+".csv")
                        zipObj.write("oura_data\calories_steps_"+date+".csv")
                    except:
                        None 
            
            #3#################################### SLEEEP

            if request.POST.get("sleep") == "on":

                for i in range(delta.days+1):

                    date = str(today + dt.timedelta(days = i))
                    # response = requests.get("https://api.fitbit.com/1.2/user/-/sleep/date/"+date+".json", headers=header).json()
                    
                    # steps = response['sleep']

                    

                    # dates = []
                    # values = []
                    # sleep_levels = []

                    # try:
                    #     intra = steps[0]['levels']['data']
                    #     for line in intra:
                    #         dates.append(line['dateTime'])
                    #         values.append(int(int(line['seconds'])/60))
                    #         sleep_levels.append(line['level'])  

                    #     with open("intraday_sleep_"+date+".csv", 'w') as csvfile:
                    #         writer = csv.writer(csvfile, lineterminator = '\n')
                    #         writer.writerow(["Timestamp", "Minutes Asleep", "Sleep Type"])
                    #         for i in range(len(dates)):
                    #             writer.writerow([dates[i], values[i], sleep_levels[i]])

                    #     zipObj.write("intraday_sleep_"+date+".csv")
                    #     os.remove("intraday_sleep_"+date+".csv")
                    # except:
                    #     None

                    try:
                        zipObj.write("oura_data\sleep_data_"+date+".csv")
                    except:
                        None 


            
            # Add multiple files to the zip
         
            # close the Zip File
            zipObj.close()
            
            file = open("sample.zip", "rb")
            response = HttpResponse(file, content_type='application/zip')  
            response['Content-Disposition'] = 'attachment; filename="oura_'+startdate+"to"+enddate+'.zip"'

            
            
            os.remove("sample.zip")

            return response

    dynamodb= boto3.resource('dynamodb',region_name='ap-south-1',aws_access_key_id='xxxxxxxxx',aws_secret_access_key='xxxxxxxxxxxxxxxx')
    tableuser = dynamodb.Table('cure_trial')
    response = tableuser.scan()    
    items = response['Items']

    context = {
        "items" : items,
        }

    return render(request,'homepage/datadownload.html', context)




@login_required(login_url="login")
def homepage(request):

    username = request.user.username
    
    dynamodb= boto3.resource('dynamodb',region_name='ap-south-1',aws_access_key_id='xxxxxxxxx',aws_secret_access_key='xxxxxxxxxxx')
    tableuser = dynamodb.Table('Userdetails')
    scan_kwargs = {
            'FilterExpression': Key('username').eq(username)
        }
    response = tableuser.scan(
            **scan_kwargs
        )
    items = response['Items'][0]
    
    tablefitbit = dynamodb.Table('fitbit')
    scan_kwargs = {
            'FilterExpression': Key('userphone').eq(items["phone"])
        }
    response = tablefitbit.scan(
            **scan_kwargs
        )
    item = response['Items'][0]

    access_token = item['token']
    header = {'accept': 'application/x-www-form-urlencoded','Authorization': 'Bearer {}'.format(access_token)}
    today = dt.date.today()
    date = str(today - dt.timedelta(days = 30))

    #Steps API call
    response = requests.get("https://api.fitbit.com/1/user/-/activities/steps/date/today/"+date+".json", headers=header).json()
    steps = response['activities-steps']
    try:
        steps_today = next((item for item in steps if item["dateTime"] == str(today)), "None")
        steps_today = steps_today['value']
    except:
        steps_today = next((item for item in steps if item["dateTime"] == str(today - dt.timedelta(days = 1))), "None")
        steps_today = steps_today['value']    
    step_dates = []
    step_values = []
    for line in steps:
        try:
            step_dates.append(line['dateTime'][5:])
            step_values.append(line['value'])
        except:
            continue
    step_dates = json.dumps(step_dates)
    step_values = json.dumps(step_values)

    #Heartrate API Call
    response = requests.get("https://api.fitbit.com/1/user/-/activities/heart/date/"+date+"/today.json", headers=header).json()
    heart = response['activities-heart']
    try:
        heart_today = next((item for item in heart if item["dateTime"] == str(today)), "None")
        heart_today = heart_today['value']['restingHeartRate']
    except:
        heart_today = next((item for item in heart if item["dateTime"] == str(today - dt.timedelta(days = 1))), "None")
        heart_today = heart_today['value']['restingHeartRate']

    heart_dates = []
    heart_values = []
    for line in heart:
        try:
            heart_dates.append(line['dateTime'][5:])
            heart_values.append(line['value']['restingHeartRate'])
        except:
            continue
    heart_dates = json.dumps(heart_dates)
    heart_values = json.dumps(heart_values)

    #Sleep API Call
    response = requests.get("https://api.fitbit.com/1.2/user/-/sleep/date/"+str(today - dt.timedelta(days = 1))+"/"+str(today)+".json", headers=header).json()
    for sleepitem in response['sleep']:
        print(sleepitem)
    sleep_today = int(int(response['sleep'][0]['duration'])/60000)
    
    #Calories API call
    response = requests.get("https://api.fitbit.com/1/user/-/activities/calories/date/today/1d.json", headers=header).json()
    calories_today = response["activities-calories"][0]["value"]

    #Floors API call
    response = requests.get("https://api.fitbit.com/1/user/-/activities/elevation/date/today/1d.json", headers=header).json()
    floors_today = int(response["activities-elevation"][0]["value"])*10

    #OURA RING API CALLS ------------------------------------------------------------------------------------------------------

    access_token = "access_token=" + "xxxxxxxxxxxxxxx"

    today = dt.date.today()
    previous = today - dt.timedelta(days = 30)

    response = requests.get("https://api.ouraring.com/v1/sleep?start="+str(previous)+"&end="+str(today)+"&"+access_token).json()
    while len(response['sleep']) == 0:
        previous = previous - dt.timedelta(days = 1)
        response = requests.get("https://api.ouraring.com/v1/sleep?start="+str(previous)+"&end="+str(today)+"&"+access_token).json()

    oura_dates = []
    oura_values = []
    oura_hr_values = []
    oura_hr_intraday = []
    for item in response['sleep']:
        oura_dates.append(item['bedtime_end'][0:10])
        oura_values.append(int(int(item['duration'])/60))
        oura_hr_values.append(item['hr_average'])
        oura_hr_intraday = item['hr_5min']
    
    previous = today - dt.timedelta(days = 30)

    response2 = requests.get("https://api.ouraring.com/v1/activity?start="+str(previous)+"&end="+str(today)+"&"+access_token).json()
    while len(response2['activity']) == 0:
        previous = previous - dt.timedelta(days = 1)
        response2 = requests.get("https://api.ouraring.com/v1/activity?start="+str(previous)+"&end="+str(today)+"&"+access_token).json()

    oura_dates2 = []
    oura_steps_values = []
    oura_calories_values = []
    oura_met_values = []
    oura_met_intraday = []
    for item in response2['activity']:
        oura_dates2.append(item['summary_date'])
        oura_steps_values.append(item['steps'])
        oura_calories_values.append(item["cal_total"])
        oura_met_values.append(item['average_met'])
        oura_met_intraday = item["met_1min"]

    context = {
        'username':username,
        'steps_today':steps_today,
        'heart_today':heart_today,
        'sleep_today':sleep_today,
        'calories_today':calories_today,
        'floors_today':floors_today,
        'heart_dates':heart_dates,
        'heart_values':heart_values,
        'step_dates':step_dates,
        'step_values':step_values,
        'oura_steps_today': oura_steps_values[-1],
        'oura_hr_today': oura_hr_values[-1],
        'oura_calories_today': oura_calories_values[-1],
        'oura_sleep_today': oura_values[-1],
        'oura_met_today': oura_met_values[-1],
        'oura_steps_values': oura_steps_values,
        'oura_steps_dates': oura_dates2,
        'oura_hr_values': oura_hr_values,
        'oura_hr_dates': oura_dates,
        'oura_calories_values': oura_calories_values,
        'oura_calories_dates': oura_dates2,
        'oura_met_values': oura_met_values,
        'oura_met_dates': oura_dates2,
        'oura_sleep_values': oura_steps_values,
        'oura_sleep_dates': oura_dates,
    }   
    return render(request,'homepage/dashboard.html', context)

@login_required(login_url="login")

def intradaypage(request):

    username = request.user.username
    
    dynamodb= boto3.resource('dynamodb',region_name='ap-south-1',aws_access_key_id='xxxxxxxxx',aws_secret_access_key='xxxxxxxxxxxxxxxxxxxxxxxx') 
    tableuser = dynamodb.Table('Userdetails')
    scan_kwargs = {
            'FilterExpression': Key('username').eq(username)
        }
    response = tableuser.scan(
            **scan_kwargs
        )
    items = response['Items'][0]
    
    tablefitbit = dynamodb.Table('fitbit')
    scan_kwargs = {
            'FilterExpression': Key('userphone').eq(items["phone"])
        }
    response = tablefitbit.scan(
            **scan_kwargs
        )
    item = response['Items'][0]

    access_token = item['token']
    header = {'accept': 'application/x-www-form-urlencoded','Authorization': 'Bearer {}'.format(access_token)}
    today = dt.date.today()
    date = str(today - dt.timedelta(days = 30))
    step_dates = []
    step_values = []
    dates=[]
    values=[]
    offsetdates = []
    offsetvalues = []
    #Steps Intraday
    response = requests.get("https://api.fitbit.com/1/user/-/activities/steps/date/today/1d/15min.json", headers=header).json()
    steps_intraday = response['activities-steps-intraday']['dataset']
    for line in steps_intraday:
        step_dates.append(line['time'][0:5])
        step_values.append(line['value'])
    if len(step_dates) < 17:
        offset = 17 - len(step_dates)
        response = requests.get("https://api.fitbit.com/1/user/-/activities/steps/date/"+str(today - dt.timedelta(days = 1))+"/1d/15min.json", headers=header).json()
        steps_intraday = response['activities-steps-intraday']['dataset']
        for line in steps_intraday:
            offsetdates.append(line['time'][0:5])
            offsetvalues.append(line['value'])
        step_dates = offsetdates[-offset:] + step_dates
        step_values = offsetvalues[-offset:] + step_values


    offsetdates = []
    offsetvalues = []
    response = requests.get("https://api.fitbit.com/1/user/-/activities/heart/date/today/1d/1min.json", headers=header).json()
    hearts_intraday = response['activities-heart-intraday']['dataset']
    for line in hearts_intraday:
        dates.append(line['time'][0:5])
        values.append(line['value'])
    if len(dates) < 241:
        offset = 241 - len(dates)
        response = requests.get("https://api.fitbit.com/1/user/-/activities/heart/date/"+str(today - dt.timedelta(days = 1))+"/1d/1min.json", headers=header).json()
        steps_intraday = response['activities-heart-intraday']['dataset']
        for line in steps_intraday:
            offsetdates.append(line['time'][0:5])
            offsetvalues.append(line['value'])
        dates = offsetdates[-offset:] + dates
        values = offsetvalues[-offset:] + values
    #Steps API call
    response = requests.get("https://api.fitbit.com/1/user/-/activities/steps/date/today/"+date+".json", headers=header).json()
    steps = response['activities-steps']
    try:
        steps_today = next((item for item in steps if item["dateTime"] == str(today)), "None")
        steps_today = steps_today['value']
    except:
        steps_today = next((item for item in steps if item["dateTime"] == str(today - dt.timedelta(days = 1))), "None")
        steps_today = steps_today['value']    
    
    step_dates = json.dumps(step_dates[-17:])
    step_values = json.dumps(step_values[-17:])

    #Heartrate API Call
    response = requests.get("https://api.fitbit.com/1/user/-/activities/heart/date/"+str(today - dt.timedelta(days = 1))+"/today.json", headers=header).json()
    heart = response['activities-heart']
    try:
        heart_today = next((item for item in heart if item["dateTime"] == str(today)), "None")
        heart_today = heart_today['value']['restingHeartRate']
    except:
        heart_today = next((item for item in heart if item["dateTime"] == str(today - dt.timedelta(days = 1))), "None")
        heart_today = heart_today['value']['restingHeartRate']


    #Sleep API Call
    response = requests.get("https://api.fitbit.com/1.2/user/-/sleep/date/"+str(today - dt.timedelta(days = 1))+"/"+str(today)+".json", headers=header).json()
    sleep_today = int(int(response['sleep'][0]['duration'])/60000)
    
    #Calories API call
    response = requests.get("https://api.fitbit.com/1/user/-/activities/calories/date/today/1d.json", headers=header).json()
    calories_today = response["activities-calories"][0]["value"]

    #Floors API call
    response = requests.get("https://api.fitbit.com/1/user/-/activities/elevation/date/today/1d.json", headers=header).json()
    floors_today = int(response["activities-elevation"][0]["value"])*10



    context = {
        'username':username,
        'steps_today':steps_today,
        'heart_today':heart_today,
        'sleep_today':sleep_today,
        'calories_today':calories_today,
        'floors_today':floors_today,
        'step_dates':step_dates,
        'step_values':step_values,
        'heart_dates':dates[-241:][0::5],
        'heart_values':values[-241:][0::5],
    }   
    return render(request,'homepage/intradaydashboard.html', context)

def profile(request):
    username = request.user.username
    
    dynamodb= boto3.resource('dynamodb',region_name='ap-south-1',aws_access_key_id='xxxxxxxxxxx',aws_secret_access_key='xxxxxxxxxxxxxxx')
    
    tableuser = dynamodb.Table('Userdetails')
    scan_kwargs = {
            'FilterExpression': Key('username').eq(username)
        }
    response = tableuser.scan(
            **scan_kwargs
        )
    items = response['Items'][0]
    
    tablefitbit = dynamodb.Table('fitbit')
    scan_kwargs = {
            'FilterExpression': Key('userphone').eq(items["phone"])
        }
    response = tablefitbit.scan(
            **scan_kwargs
        )
    item = response['Items'][0]

    access_token = item['token']
    header = {'accept': 'application/x-www-form-urlencoded','Authorization': 'Bearer {}'.format(access_token)}

    response = requests.get("https://api.fitbit.com/1/user/-/profile.json", headers=header).json()
    print("lets fooooooo")
    fitbitprofile = response['user']
    
    fullname = fitbitprofile['fullName']
    gender = fitbitprofile['gender']
    height = fitbitprofile['height']
    dob = fitbitprofile['dateOfBirth']
    weight = fitbitprofile['weight']

    context = {
        'fullname':fullname,
        "gender":gender,
        "height":height,
        "dob":dob,
        "weight":weight,
    }
    return render(request, 'homepage/profile.html',context)

def logout(request):
    auth.logout(request)
    return redirect('login')


class ajaxHandlerView(View):
    def get(self, request):
        device = request.GET.get('devname')
        print(device)

        username = request.user.username
    
        dynamodb= boto3.resource('dynamodb',region_name='ap-south-1',aws_access_key_id='xxxxxxxxxx',aws_secret_access_key='xxxxxxxxxxxxxxx')
        tableuser = dynamodb.Table('Userdetails')
        scan_kwargs = {
                'FilterExpression': Key('username').eq(username)
            }
        response = tableuser.scan(
                **scan_kwargs
            )
        items = response['Items'][0]
        
        tablefitbit = dynamodb.Table('fitbit')
        scan_kwargs = {
                'FilterExpression': Key('userphone').eq(items["phone"])
            }
        response = tablefitbit.scan(
                **scan_kwargs
            )
        item = response['Items'][0]

        access_token = item['token']
        header = {'accept': 'application/x-www-form-urlencoded','Authorization': 'Bearer {}'.format(access_token)}
        today = dt.date.today()
        date = str(today - dt.timedelta(days = 30))

        #Steps API call
        dates = []
        values = []
        if device == "Steps":
            response = requests.get("https://api.fitbit.com/1/user/-/activities/steps/date/today/"+date+".json", headers=header).json()
            print(response)
            steps = response['activities-steps']        
            for line in steps:
                try:
                    dates.append(line['dateTime'][5:])
                    values.append(line['value'])
                except:
                    continue
        #HEARTRATE
        elif device == "Resting HeartRate":
            response = requests.get("https://api.fitbit.com/1/user/-/activities/heart/date/"+date+"/today.json", headers=header).json()
            heart = response['activities-heart']
            print(heart)
            for line in heart:
                try:
                    dates.append(line['dateTime'][5:])
                    values.append(line['value']['restingHeartRate'])
                except:
                    continue
        # CALORIES
        elif device == "Calories":
            response = requests.get("https://api.fitbit.com/1/user/-/activities/calories/date/today/"+date+".json", headers=header).json()
            print(response)
            steps = response['activities-calories']        
            for line in steps:
                try:
                    dates.append(line['dateTime'][5:])
                    values.append(line['value'])
                except:
                    continue
        # ELEVATION
        elif device == "Elevation":
            response = requests.get("https://api.fitbit.com/1/user/-/activities/elevation/date/today/"+date+".json", headers=header).json()
            print(response)
            steps = response['activities-elevation']        
            for line in steps:
                try:
                    dates.append(line['dateTime'][5:])
                    values.append(int(line['value'])*10)
                except:
                    continue
        # SLEEP
        elif device == "Minutes Asleep":
            response = requests.get("https://api.fitbit.com/1.2/user/-/sleep/date/"+date+"/"+str(today)+".json", headers=header).json()
            steps = response['sleep']
            for line in steps:
                try:
                    dates.append(line['dateOfSleep'][5:])
                    values.append(int(int(line['duration'])/60000))
                except:
                    continue
            dates.reverse()
            values.reverse()
        
        if request.is_ajax():
            return JsonResponse({'name': device, 'step_dates': dates, 'step_values': values}, status = 200)
        
        return redirect("homepage")

class intradayAjaxHandlerView(View):
    def get(self, request):
        device = request.GET.get('devname')
        print(device)

        username = request.user.username
    
        dynamodb= boto3.resource('dynamodb',region_name='ap-south-1',aws_access_key_id='xxxxxxxxxxxxxxxxxxx',aws_secret_access_key='xxxxxxxxxxxxxxxxxxxxx')
        
        tableuser = dynamodb.Table('Userdetails')
        scan_kwargs = {
                'FilterExpression': Key('username').eq(username)
            }
        response = tableuser.scan(
                **scan_kwargs
            )
        items = response['Items'][0]
        
        tablefitbit = dynamodb.Table('fitbit')
        scan_kwargs = {
                'FilterExpression': Key('userphone').eq(items["phone"])
            }
        response = tablefitbit.scan(
                **scan_kwargs
            )
        item = response['Items'][0]

        access_token = item['token']
        header = {'accept': 'application/x-www-form-urlencoded','Authorization': 'Bearer {}'.format(access_token)}
        today = dt.date.today()
        date = str(today - dt.timedelta(days = 30))
       
        #Steps API call
        dates = []
        values = []
        offsetdates = []
        offsetvalues = []
        bg_colour = []
        if device == "Steps":
            response = requests.get("https://api.fitbit.com/1/user/-/activities/steps/date/today/1d/15min.json", headers=header).json()
            steps_intraday = response['activities-steps-intraday']['dataset']
            for line in steps_intraday:
                dates.append(line['time'][0:5])
                values.append(line['value'])
            if len(dates) < 17:
                offset = 17 - len(dates)
                response = requests.get("https://api.fitbit.com/1/user/-/activities/steps/date/"+str(today - dt.timedelta(days = 1))+"/1d/15min.json", headers=header).json()
                steps_intraday = response['activities-steps-intraday']['dataset']
                for line in steps_intraday:
                    offsetdates.append(line['time'][0:5])
                    offsetvalues.append(line['value'])
                dates = offsetdates[-offset:] + dates
                values = offsetvalues[-offset:] + values

            dates = dates[-17:]
            values = values[-17:]
        #HEARTRATE
        elif device == "HeartRate":
            response = requests.get("https://api.fitbit.com/1/user/-/activities/heart/date/today/1d/1min.json", headers=header).json()
            steps_intraday = response['activities-heart-intraday']['dataset']
            for line in steps_intraday:
                dates.append(line['time'][0:5])
                values.append(line['value'])

            if len(dates) < 241:
                offset = 241 - len(dates)
                response = requests.get("https://api.fitbit.com/1/user/-/activities/heart/date/"+str(today - dt.timedelta(days = 1))+"/1d/1min.json", headers=header).json()
                steps_intraday = response['activities-heart-intraday']['dataset']
                for line in steps_intraday:
                    offsetdates.append(line['time'][0:5])
                    offsetvalues.append(line['value'])
                dates = offsetdates[-offset:] + dates
                values = offsetvalues[-offset:] + values
            dates = dates[-241:][0::5]
            values = values[-241:][0::5]
        # CALORIES
        elif device == "Calories":
            response = requests.get("https://api.fitbit.com/1/user/-/activities/calories/date/today/1d/15min.json", headers=header).json()
            steps_intraday = response['activities-calories-intraday']['dataset']
            for line in steps_intraday:
                dates.append(line['time'][0:5])
                values.append(line['value'])

            if len(dates) < 17:
                offset = 17 - len(dates)
                response = requests.get("https://api.fitbit.com/1/user/-/activities/calories/date/"+str(today - dt.timedelta(days = 1))+"/1d/15min.json", headers=header).json()
                steps_intraday = response['activities-calories-intraday']['dataset']
                for line in steps_intraday:
                    offsetdates.append(line['time'][0:5])
                    offsetvalues.append(line['value'])
                dates = offsetdates[-offset:] + dates
                values = offsetvalues[-offset:] + values
            dates = dates[-17:]
            values = values[-17:]
        # ELEVATION
        elif device == "Elevation":
            response = requests.get("https://api.fitbit.com/1/user/-/activities/elevation/date/today/1d/15min.json", headers=header).json()
            steps_intraday = response['activities-elevation-intraday']['dataset']
            for line in steps_intraday:
                dates.append(line['time'][0:5])
                values.append(int(line['value'])*10)

            if len(dates) < 17:
                offset = 17 - len(dates)
                response = requests.get("https://api.fitbit.com/1/user/-/activities/elevation/date/"+str(today - dt.timedelta(days = 1))+"/1d/15min.json", headers=header).json()
                steps_intraday = response['activities-elevation-intraday']['dataset']
                for line in steps_intraday:
                    offsetdates.append(line['time'][0:5])
                    offsetvalues.append(line['value'])
                dates = offsetdates[-offset:] + dates
                values = offsetvalues[-offset:] + values
            dates = dates[-17:]
            values = values[-17:]
        # SLEEP
        elif device == "Minutes Asleep":
            response = requests.get("https://api.fitbit.com/1.2/user/-/sleep/date/"+str(today - dt.timedelta(days = 1))+"/"+str(today)+".json", headers=header).json()
            steps = response['sleep']
            intra = steps[0]['levels']['data']
            for line in intra:
                dates.append(line['dateTime'][11:16])
                values.append(int(int(line['seconds'])/60))
                if line['level'] == "wake":
                    bg_colour.append('rgba(255, 200, 200, 0.8)')
                elif line['level'] == "deep":
                    bg_colour.append('rgba(200, 200, 255, 0.8)')
                elif line['level'] == "light":
                    bg_colour.append('rgba(200, 255, 200, 0.8)')
                else:
                    bg_colour.append('rgba(255, 255, 255, 0.8)')
        
        print(bg_colour)
        if request.is_ajax():
            return JsonResponse({'name': device, 'step_dates': dates, 'step_values': values, 'bg_colour':bg_colour}, status = 200)
        
        return redirect("homepage")
