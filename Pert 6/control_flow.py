import streamlit as st 
import pandas as pd
import numpy as np

# 9. Control Flow

st.title("Control Flow")

#st.stop
st.subheader("Stop Execution")

name = st.text_input('Name')
if not name:
  st.warning('Please input a name.')
  st.stop()
st.success('Thank you for inputting a name.')

#st.experimental
st.subheader("Rerun Script")

st.experimental_rerun()
