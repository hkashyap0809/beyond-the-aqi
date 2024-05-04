import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from keras.preprocessing.image import img_to_array, load_img
from tensorflow.keras.applications.inception_v3 import preprocess_input
import matplotlib.pyplot as plt
import numpy as np

def predict():
    imgPath = st.session_state['uploaded_file']
    print(imgPath)
    model = load_model('./models/model_inception.h5')
    img = load_img(imgPath, target_size=(224, 224))
    x = img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    p = np.argmax(model.predict(x))
    if p == 0:
        st.title("Irrelevant data")
    elif p == 1:
        st.title("Moderate pollution")
    elif p == 2:
        st.title("No pollution")
    elif p == 3:
        st.title("Severe pollution")

def aqi_image_prediction_component():
    st.title("Image Prediction")
    uploaded_file = st.file_uploader("Choose a file", accept_multiple_files=False)
    if uploaded_file is not None:
        st.session_state['uploaded_file'] = uploaded_file
    if "uploaded_file" in st.session_state:
        st.image(uploaded_file)
        predict()