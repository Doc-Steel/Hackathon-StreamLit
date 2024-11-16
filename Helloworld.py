import streamlit as st
import requests
from PIL import Image
from io import BytesIO

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
countries = ["Kenya", "Sri Lanka", "United States", "United Kingdom"]

# Streamlit App
st.title("Flags of Selected Countries")

for country in countries:
    flag_image = fetch_flag_image(country)
    if flag_image:
        st.image(flag_image, caption=f"Flag of {country}", use_container_width=True)
    else:
        st.error(f"Flag not found for {country}.")
