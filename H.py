import streamlit as st
import pycountry
import random

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

def wrong_button():
    st.session_state.clicked = True
    st.session_state.playerCorrect = False

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

# Handle player name input (allow only once)
if 'name' not in st.session_state or st.session_state.name == "":
    player_name = st.text_input("Enter Your Name")
    if player_name:
        st.session_state.name = player_name  # Store the name once it's entered
        st.write(f'Hello, {st.session_state.name}!')
else:
    st.write(f'Hello, {st.session_state.name}!')

# Create a large empty space using markdown
st.markdown("<br>" * 10, unsafe_allow_html=True)  # This will create 50 blank lines

# Or using st.empty() to leave a placeholder
st.empty()

# Define the layout for the buttons
column1, column2, column3, column4 = st.columns(4)

# Randomize the positions of the buttons
column1.button(other_countries[0], on_click=correct_button if other_countries[0] == chosen_country else wrong_button)
column2.button(other_countries[1], on_click=correct_button if other_countries[1] == chosen_country else wrong_button)
column3.button(other_countries[2], on_click=correct_button if other_countries[2] == chosen_country else wrong_button)
column4.button(other_countries[3], on_click=correct_button if other_countries[3] == chosen_country else wrong_button)

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
