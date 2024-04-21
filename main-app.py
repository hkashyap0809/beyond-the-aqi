import streamlit as st
import time
from aqi_data import aqi_data_component
from aqi_gpt import aqi_gpt_component
from aqi_image_prediction import aqi_image_prediction_component
from aqi_prediction import aqi_prediction

def main():
    st.title("BEYOND THE AQI")
    # tab1, tab2, tab3, tab4 = st.tabs(["AQI DATA", "AQI PREDICTION", "AQI GPT", "IMAGE PREDICTION"])
    tab1, tab3, tab4 = st.tabs(["AQI DATA", "AQI GPT", "IMAGE PREDICTION"])
    with tab1:
        aqi_data_component()
    # with tab2:
    #     aqi_prediction()
    with tab3:
        aqi_gpt_component()
    with tab4:
        aqi_image_prediction_component()

if __name__ == "__main__":
    main()
