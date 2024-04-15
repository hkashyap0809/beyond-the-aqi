import streamlit as st
import time
from aqi_data import aqi_data_component
from aqi_gpt import aqi_gpt_component
from aqi_image_prediction import aqi_image_prediction_component



if st.sidebar.button("AQI DATA"):
    aqi_data_component()  

if st.sidebar.button("AQI GPT"):
    aqi_gpt_component()


if st.sidebar.button("Image prediction"):
    aqi_image_prediction_component()
