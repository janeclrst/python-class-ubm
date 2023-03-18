import streamlit as st 
import pandas as pd
import numpy as np
from PIL import Image

# 5. Media Element

st.title("Media Element")

#st.image
st.subheader("Image")

image = Image.open('sunrise.jpg')

st.image(image, caption='Sunrise by the mountains')

#st.audio
st.subheader("Audio")

audio_file = open('myaudio.ogg', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/ogg')

sample_rate = 44100  # 44100 samples per second
seconds = 2  # Note duration of 2 seconds
frequency_la = 440  # Our played note will be 440 Hz
# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
t = np.linspace(0, seconds, seconds * sample_rate, False)
# Generate a 440 Hz sine wave
note_la = np.sin(frequency_la * t * 2 * np.pi)

st.audio(note_la, sample_rate=sample_rate)

#st.video
st.subheader("Video")

video_file = open('myvideo.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)