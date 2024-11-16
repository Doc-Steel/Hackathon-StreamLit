import streamlit as st
import pycountry
import random
import requests
from PIL import Image
from io import BytesIO

# Initialize session state variables
if 'playerCorrect' not in st.session_state:
    st.session_state.playerCorrect = False
if 'clicked' not in st.session_state:
    st.session_state.clicked = False
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'name' not in st.session_state:
    st.session_state.name = ""

# Functions for correct and wrong buttons
def correct_button():
    st.session_state.clicked = True
    st.session_state.score += 1
    st.session_state.playerCorrect = True
    st.success("Correct!!!")  # Green popup for correct answer

def wrong_button():
    st.session_state.clicked = True
    st.session_state.playerCorrect = False
    st.error("Wrong!!!")  # Green popup for correct answer

# Function to fetch the flag of a country
def fetch_flag_image(country_name):
    search_url = f"https://restcountries.com/v3.1/name/{country_name}"
    try:
        response = requests.get(search_url)
        response.raise_for_status()
        country_data = response.json()
        flag_url = country_data[0]['flags']['png']
        response = requests.get(flag_url)
        return Image.open(BytesIO(response.content))
    except Exception as e:
        st.error(f"Error fetching flag for {country_name}: {e}")
        return None

# Generate a list of country names
country_names = [country.name for country in pycountry.countries]

# Choose a random country
chosen_country = random.choice(country_names)

# Choose three other random names for buttons, excluding the chosen country
other_countries = random.sample([name for name in country_names if name != chosen_country], 3)

# Append the chosen country to the list
other_countries.append(chosen_country)

# Shuffle the list of countries (including the correct one)
random.shuffle(other_countries)

# Streamlit UI
st.title("Fun with Flags")

# Display only the correct flag (for the chosen country)
for i, country in enumerate(other_countries):
    if country == chosen_country:
        # Fetch and display the flag for the chosen country
        flag_image = fetch_flag_image(country)
        if flag_image:
            st.image(flag_image, caption=f"Guess this Flag!", width=300)  # Resize flag for smaller display
        else:
            st.error(f"Flag not found for {country}.")

# Define the layout for the buttons
column1, column2, column3, column4 = st.columns(4)

# Randomize the positions of the buttons
button_functions = [correct_button if country == chosen_country else wrong_button for country in other_countries]

column1.button(other_countries[0], on_click=button_functions[0])
column2.button(other_countries[1], on_click=button_functions[1])
column3.button(other_countries[2], on_click=button_functions[2])
column4.button(other_countries[3], on_click=button_functions[3])

# Display result
with st.empty():
    if st.session_state.clicked:
        if st.session_state.playerCorrect:
            st.write("Correct!!!")
        else:
            st.write("WRONG!!!")
    else:
        pass

# Display score
st.write(f"Your score: {st.session_state.score}")
