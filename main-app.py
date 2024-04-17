import streamlit as st
import time
from aqi_data import aqi_data_component
from aqi_gpt import aqi_gpt_component
from aqi_image_prediction import aqi_image_prediction_component

def main():
    st.title("BEYOND THE AQI")
    tab1, tab2, tab3 = st.tabs(["AQI DATA", "AQI GPT", "IMAGE PREDICTION"])
    with tab1:
        aqi_data_component()
    with tab2:
        aqi_gpt_component()
    with tab3:
        aqi_image_prediction_component()

if __name__ == "__main__":
    main()
