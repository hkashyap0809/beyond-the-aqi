import streamlit as st
import pandas as pd
import requests
from tensorflow.keras.models import load_model
import random
import joblib
import http.client
import json

def fetch_api_data(city):
    # api_key = 'bb051e7654f0459697a0dd35ca84ad69'
    # api_key = '015423943a4b47b8851fcef8976b304b'
    # Ambee API
    api_key = 'ad220e078d6771f89706cdcc04c3220f8111455ac5aeeb77708c92df02bb05fc'
    # url = f'https://api.weatherbit.io/v2.0/current/airquality?city={city}&key={api_key}'
    url = f'/latest/by-city?city={city}'
    # response = requests.get(url)
    # return response.json()

    conn = http.client.HTTPSConnection("api.ambeedata.com")

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

def aqi_prediction():
    st.title("AQI PREDICTION")
    model = load_model('./models/aqi_pred_model.h5')
    loaded_scaler = joblib.load('./models/scaler.pkl')
    df = pd.read_csv('./final_data.csv')
    cities = df['City'].unique()
    selected_city = st.selectbox('Select city', cities, key="prediction")
    print(selected_city)
    # api_response = fetch_api_data(selected_city)
    parsed_response = fetch_api_data(selected_city)
    station = parsed_response.get("stations", [])[0]
    co_value = station.get("CO")
    no2_value = station.get("NO2")
    o3_value = station.get("OZONE")
    pm25_value = station.get("PM25")
    pm10_value = station.get("PM10")
    aqi = station.get("AQI")

    # co_value = api_response['data'][0]['co']
    # o3_value = api_response['data'][0]['o3']
    # pm25_value = api_response['data'][0]['pm25']
    # pm10_value = api_response['data'][0]['pm10']
    # no2_value = api_response['data'][0]['no2']
    # aqi = api_response['data'][0]['aqi']

    val = random.uniform(5, 20)
    st.write("Current CO value: ", co_value)
    st.write("Current O3 value: ", o3_value)
    st.write("Current PM2.5 value: ", pm25_value)
    st.write("Current PM10 value: ", pm10_value)
    st.write("Current NO2 value: ", no2_value)
    user_input = pd.DataFrame({
        'PM25': [pm25_value],
        'PM10': [pm10_value],
        'O3': [o3_value],
        'CO': [co_value],
        'NO2': [no2_value]
    })
    scaled_data_point = loaded_scaler.transform(user_input)
    prediction = model.predict(scaled_data_point)
    st.write("Actual AQI is: ", aqi)
    st.write("Predicted AQI is: ", prediction)

