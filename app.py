import tensorflow as tf
from tensorflow.keras import models
import numpy as np
import cv2
import streamlit as st
import os

# Load the pre-trained emotion classification model
model = models.load_model('model/human_emotion_classifier.keras')
categories = [
    ['angry'],
    ['disgust'],
    ['fear'],
    ['happy'],
    ['neutral'],
    ['sad'],
    ['surprise']
]

# Streamlit app for human emotion recognition
st.header('Human Emotion Recognition')
image_path = st.text_input('Enter Image Path')
if image_path:
    img = cv2.imread(image_path)[:, :, 0]
    img = cv2.resize(img, (48, 48))
    img = np.invert(np.array([img]))

    output = model.predict(img)
    predict_cat = categories[np.argmax(output)]

    display = f'Input emotion is **{predict_cat[0]}**'
    st.markdown(display)

    img_name = os.path.basename(image_path)
    st.image(f'testData/{img_name}', width=300)
else:
    st.warning('Please enter a valid image path.')

