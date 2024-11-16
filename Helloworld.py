import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import pycountry
import random

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

# List of countries
countries = [country.name for country in pycountry.countries]

# Streamlit App
st.title("Flags of Randomly Selected Countries")

# Select 4 random unique countries
selected_countries = random.sample(countries, 4)

# Display flags in a 2x2 grid
cols = st.columns(2)  # Create two columns for the grid
for i, country in enumerate(selected_countries):
    flag_image = fetch_flag_image(country)
    with cols[i % 2]:  # Alternate between the two columns
        if flag_image:
            st.image(flag_image, caption=f"Flag of {country}", width=150)  # Resize flag for smaller display
        else:
            st.error(f"Flag not found for {country}.")
