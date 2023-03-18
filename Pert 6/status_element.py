import streamlit as st 
import pandas as pd
import numpy as np
from datetime import time

# 8. Status Element

st.title("Status Element - Display Progress and Status")

#st.progress
st.subheader("Progress bar")

progress_text = "Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1, text=progress_text)

#st.spinner
st.subheader("Spinner")

with st.spinner('Wait for it...'):
    time.sleep(5)
st.success('Done!')

#st.balloons
st.subheader("Balloons")

st.balloons()

#st.snowflakes
st.subheader("Snowflakes")

st.snow()

#st.error
st.subheader("Error Box")

st.error('This is an error', icon="🚨")

#st.warning
st.subheader("Warning Box")

st.warning('This is a warning', icon="⚠️")

#st.info
st.subheader("Info Box")

st.info('This is a purely informational message', icon="ℹ️")

#st.success
st.subheader("Success Box")

st.success('This is a success message!', icon="✅")

#st.exception
st.subheader("Exception Output")

e = RuntimeError('This is an exception of type RuntimeError')
st.exception(e)


