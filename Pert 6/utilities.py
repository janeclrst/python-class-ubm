import streamlit as st 
import pandas as pd
import numpy as np

# 10. Utilities

st.title("Utilities")

#st.set_page_config
st.subheader("Set Page Title, Favicon, and more")

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

#st.echo
st.subheader("Echo")

with st.echo():
    st.write('This code will be printed')
    
# Display Code

def get_user_name():
    return 'John'

# ------------------------------------------------
# Want people to see this part of the code...

def get_punctuation():
    return '!!!'

greeting = "Hi there, "
user_name = get_user_name()
punctuation = get_punctuation()

st.write(greeting, user_name, punctuation)

# ...up to here
# ------------------------------------------------

foo = 'bar'
st.write('Done!')    

#or

def get_user_name():
    return 'John'

with st.echo():
    # Everything inside this block will be both printed to the screen
    # and executed.

    def get_punctuation():
        return '!!!'

    greeting = "Hi there, "
    value = get_user_name()
    punctuation = get_punctuation()

    st.write(greeting, value, punctuation)

# And now we're back to _not_ printing to the screen
foo = 'bar'
st.write('Done!')

#st.set_help
st.subheader("Help")

#st.experimental_show
st.subheader("Experimental Show")

dataframe = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
})
st.experimental_show(dataframe)

#st.experimental_get_query_params
st.subheader("Experimental Get Query Params")

st.experimental_get_query_params()
{"show_map": ["True"], "selected": ["asia", "america"]}

#st.experimental_set_query_params
st.subheader("Experimental Set Query Params")

st.experimental_set_query_params(
    show_map=True,
    selected=["asia", "america"],
)

