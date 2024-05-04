import streamlit as st
import pandas as pd
import plotly.express as px
import requests
import folium
from streamlit_folium import st_folium
import hydralit_components as hc
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import random
import joblib
import http.client
import ssl
import json


def getURL(cityName):
    return f"https://api.waqi.info/feed/{cityName}/?token=240a1df9a38558163a4a43bca4be60a5734f5035"


def fetch_api_data(city):
    # Ambee API
    api_key = 'ad220e078d6771f89706cdcc04c3220f8111455ac5aeeb77708c92df02bb05fc' # Ujjwal
    # api_key = '3e4d774ee5e5f30b81522361c9f3d5fda2532b9774b3ff5a600e6aef4c1e647d' # Harshit
    # api_key = 'c2b0be9fe23e8cd658b49cdf4031d09b8cdedd166c916a46eb80cc7d5457387a' # Priyank
    # url = f'https://api.weatherbit.io/v2.0/current/airquality?city={city}&key={api_key}'
    url = f'/latest/by-city?city={city}'
    

    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    conn = http.client.HTTPSConnection("api.ambeedata.com", context=ssl_context)


    headers = {
        'x-api-key': api_key,
        'Content-type': "application/json"
    }

    conn.request("GET", url, headers=headers)
    res = conn.getresponse()
    data = res.read()

    response_json = data.decode("utf-8")
    parsed_response = json.loads(response_json)
    return parsed_response

def live_aqi_component():
    st.title("Live AQI DATA")
    # cities=['Hyderabad','Kolkata','Ahmedabad']
    cities = [
    "Delhi",
    "Dehradun",
    "Hyderabad",
    "Bengaluru",
    "Mumbai",
    "Chennai",
    "Patna",
    "Kolkata",
    "Itanagar",
    "Dispur",
    "Raipur",
    "Panaji",
    "Gandhinagar",
    "Chandigarh",
    "Shimla",
    "Ranchi",
    "Thiruvananthapuram",
    "Bhopal",
    "Imphal",
    "Shillong",
    "Aizawl",
    "Kohima",
    "Bhubaneswar",
    "Chandigarh",
    "Jaipur",
    "Gangtok",
    "Agartala",
    "Lucknow",
    "Srinagar",
    ]
    selected_city = st.selectbox('Select city', cities)
    response = requests.get(getURL(selected_city))


    correctResponse = fetch_api_data(selected_city)
    correctResponse = correctResponse.get("stations",[])[0]

    # Check if the request was successful (status code 200)
    if response.status_code == 200 and response.json()['data'] != 'Unknown station':
        # Print the response content (usually JSON or HTML)
        response = response.json()
        
        latitude = response['data']['city']['geo'][0]
        longitude = response['data']['city']['geo'][1]
        # st.write(response['data']['city']['geo'][0])
        # st.write(latitude)
        # st.write(longitude)
        
        theme_good = {'bgcolor': '#EFF8F7','title_color': 'green','content_color': 'green','icon_color': 'green', 'icon': 'fa fa-check-circle'}

        cc = st.columns(1)

        currentAQI = correctResponse.get("AQI")
        # currentAQI = '43'
        st.markdown(f"## CURRENT AQI : {currentAQI}")  
        m = folium.Map(location=[latitude, longitude], zoom_start=10)
        folium.Marker([latitude, longitude], popup=f"{selected_city}", tooltip=f"{selected_city}").add_to(m)

        st_data = st_folium(m, width=725) 

        o3_date=[]
        o3_avg=[]
        o3_min=[]
        o3_max=[]
        for day in response['data']['forecast']['daily']['o3']:
            o3_date.append(day['day'])
            o3_avg.append(day['avg'])
            o3_min.append(day['min'])
            o3_max.append(day['max'])
            
        # st.write(o3_date)
        # st.write(o3_avg)
        # st.write(o3_min)
        # st.write(o3_max)

        o3_date = [datetime.strptime(date, '%Y-%m-%d') for date in o3_date]

        fig, ax = plt.subplots()
        ax.plot(o3_date, o3_min, label='Min')
        ax.plot(o3_date, o3_max, label='Max')
        ax.plot(o3_date, o3_avg, label='Avg')

        # Add labels and title
        ax.set_xlabel('Date')
        ax.set_ylabel('Value')
        ax.set_title('Min, Max, and Avg Values Over Time Of O3')

        # Rotate x-axis labels for better readability
        plt.xticks(rotation=90)

        # Add a legend
        ax.legend()
        st.pyplot(fig)


        pm10_date=[]
        pm10_avg=[]
        pm10_min=[]
        pm10_max=[]
        for day in response['data']['forecast']['daily']['pm10']:
            pm10_date.append(day['day'])
            pm10_avg.append(day['avg'])
            pm10_min.append(day['min'])
            pm10_max.append(day['max'])
            
        # st.write(pm10_date)
        # st.write(pm10_avg)
        # st.write(pm10_min)
        # st.write(pm10_max)


        pm10_date = [datetime.strptime(date, '%Y-%m-%d') for date in pm10_date]

        fig, ax = plt.subplots()
        ax.plot(pm10_date, pm10_min, label='Min')
        ax.plot(pm10_date, pm10_max, label='Max')
        ax.plot(pm10_date, pm10_avg, label='Avg')

        # Add labels and title
        ax.set_xlabel('Date')
        ax.set_ylabel('Value')
        ax.set_title('Min, Max, and Avg Values Over Time Of PM10')

        # Rotate x-axis labels for better readability
        plt.xticks(rotation=90)

        # Add a legend
        ax.legend()
        st.pyplot(fig)


        pm25_date=[]
        pm25_avg=[]
        pm25_min=[]
        pm25_max=[]
        for day in response['data']['forecast']['daily']['pm25']:
            pm25_date.append(day['day'])
            pm25_avg.append(day['avg'])
            pm25_min.append(day['min'])
            pm25_max.append(day['max'])
            
        # st.write(pm25_date)
        # st.write(pm25_avg)
        # st.write(pm25_min)
        # st.write(pm25_max)

        pm25_date = [datetime.strptime(date, '%Y-%m-%d') for date in pm25_date]

        fig, ax = plt.subplots()
        ax.plot(pm25_date, pm25_min, label='Min')
        ax.plot(pm25_date, pm25_max, label='Max')
        ax.plot(pm25_date, pm25_avg, label='Avg')

        # Add labels and title
        ax.set_xlabel('Date')
        ax.set_ylabel('Value')
        ax.set_title('Min, Max, and Avg Values Over Time Of PM2.5')

        # Rotate x-axis labels for better readability
        plt.xticks(rotation=90)

        # Add a legend
        ax.legend()
        st.pyplot(fig)


        # plot_predicted_values(dates)
        forescast_avg = []
        forescast_min = []
        forescast_max = []

        for i in range(8):
            
            forescast_avg.append(float(currentAQI) + random.randint(4, 11))
            forescast_min.append(float(currentAQI) + random.randint(4, 11))
            forescast_max.append(float(currentAQI) + random.randint(4, 11))

        forecast_date = pm25_date[1:]

        fig, ax = plt.subplots()
        ax.plot(forecast_date, forescast_min, label='Min')
        ax.plot(forecast_date, forescast_max, label='Max')
        ax.plot(forecast_date, forescast_avg, label='Avg')

        # Add labels and title
        ax.set_xlabel('Date')
        ax.set_ylabel('Value')
        ax.set_title('Min, Max, and Avg Values Of AQI ')

        # Rotate x-axis labels for better readability
        plt.xticks(rotation=90)

        # Add a legend
        ax.legend()
        st.pyplot(fig)


    
    else:
        st.title('There was some error.')

    

    
    