import streamlit as st
import time
from aqi_data import aqi_data_component
from aqi_gpt import aqi_gpt_component
from aqi_image_prediction import aqi_image_prediction_component
from aqi_prediction import aqi_prediction
from aqi_live import live_aqi_component

def main():
    st.title("BEYOND THE AQI")
    tab1, tab2, tab3, tab4= st.tabs(["AQI DATA", "AQI PREDICTION", "LIVE AQI DATA", "IMAGE PREDICTION"])
    with tab1:
        aqi_data_component()
    with tab2:
        aqi_prediction()
    with tab3:
        live_aqi_component()
    with tab4:
        aqi_image_prediction_component()

if __name__ == "__main__":
    main()
