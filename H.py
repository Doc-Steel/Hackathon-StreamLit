import streamlit as st
import numpy as np
import pandas as pd
import pycountry
import random

score = 0
playerName = ""
playerCorrect = False

def correct_button():
    st.session_state.clicked = True
    st.session_state.score += 1
    st.session_state.playerCorrect = True

def wrong_button():
    st.session_state.clicked = True
    st.session_state.playerCorrect = False

# Generate a list of country names
country_names = [country.name for country in pycountry.countries]

# Choose a random country
chosen_country = random.choice(country_names)

# Choose three other random names for buttons, excluding the chosen country
other_countries = random.sample([name for name in country_names if name != chosen_country], 3)


st.title("Mass RPG")

st.text_input("Enter Your Name", key="name")
st.write('Your name is ', st.session_state.name)

if 'playerCorrect' not in st.session_state:
    st.session_state.playerCorrect = False
if 'clicked' not in st.session_state:
    st.session_state.clicked = False
if 'score' not in st.session_state:
    st.session_state.score = 0

column1, column2, column3, column4  = st.columns(4)
# You can use a column just like st.sidebar:
column1.button(chosen_country, on_click=correct_button)
column2.button(other_countries[0], on_click=wrong_button)
column3.button(other_countries[1], on_click=wrong_button)
column4.button(other_countries[2], on_click=wrong_button)

with st.empty():
    if st.session_state.clicked:
        if st.session_state.playerCorrect == True:
            st.write("Correct!!!")
            pass
        else:
            st.write("WRONG!!!")
            pass
    else:    
        pass