import streamlit as st 
import pandas as pd
import numpy as np
import altair as alt
import numpy as np

# 1. Write and Magic

st.title("Write and Magic")

#st.write
st.subheader("st.write:")

st.write('Hello, *World!* :sunglasses:') 

st.write(1234)
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
}))

data_frame= pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
})
st.write('1 + 1 = ', 2)
st.write('Below is a DataFrame:', data_frame, 'Above is a dataframe.')

df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.write(c)


#Magic
st.subheader("Magic:")
# Draw a title and some text to the app:
'''
# This is the document title

This is some _markdown_.
'''
df = pd.DataFrame({'col1': [1,2,3]})
df  # 👈 Draw the dataframe

x = 10
'x', x  # 👈 Draw the string 'x' and then the value of x





