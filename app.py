
import streamlit as st
from dotenv import load_dotenv
import os
import googlemaps
import requests

# Load environment variables
load_dotenv()

# Configure Google Maps client
gmaps = googlemaps.Client(key=os.getenv("GOOGLE_MAPS_API_KEY"))
weather_api_key = os.getenv("WEATHER_API_KEY")

# Function to calculate distance and duration between two locations
def get_distance(origin, destination):
    try:
        distance_matrix = gmaps.distance_matrix(origins=origin, destinations=destination)
        if distance_matrix['status'] == 'OK':
            elements = distance_matrix['rows'][0]['elements'][0]
            if elements['status'] == 'OK':
                distance = elements['distance']['text']
                duration = elements['duration']['text']
                return distance, duration
            else:
                return "Error: " + elements['status'], None
        else:
            return "Error: " + distance_matrix['status'], None
    except Exception as e:
        return str(e), None

# Function to get weather details
def get_weather(location):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={weather_api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
            weather_desc = weather_data['weather'][0]['description']
            temp = weather_data['main']['temp']
            return weather_desc, temp
        else:
            return "Error: Could not retrieve weather data", None
    except Exception as e:
        return str(e), None

# Function to get places of interest like hotels and restaurants
def get_places(location, place_type):
    try:
        places = gmaps.places_nearby(location=location, radius=5000, type=place_type)
        if places['status'] == 'OK':
            return [place['name'] for place in places['results']]
        else:
            return ["Error: " + places['status']]
    except Exception as e:
        return [str(e)]

# Streamlit UI
st.title("Google Maps Enhanced Insights 📍➡️📍")

origin = st.text_input("Enter the Origin Location:", placeholder="e.g., Kannur")
destination = st.text_input("Enter the Destination Location:", placeholder="e.g., Kozhikode")

if st.button("Get Insights 🚗"):
    if origin and destination:
        distance, duration = get_distance(origin, destination)
        weather_origin_desc, weather_origin_temp = get_weather(origin)
        weather_dest_desc, weather_dest_temp = get_weather(destination)
        hotels_origin = get_places(origin, "lodging")
        restaurants_origin = get_places(origin, "restaurant")
        hotels_destination = get_places(destination, "lodging")
        restaurants_destination = get_places(destination, "restaurant")

        if distance and duration:
            st.markdown("## Distance and Duration:")
            st.write(f"Distance: {distance}")
            st.write(f"Duration: {duration}")

        if weather_origin_desc and weather_origin_temp:
            st.markdown(f"## Weather at {origin}:")
            st.write(f"Weather: {weather_origin_desc}")
            st.write(f"Temperature: {weather_origin_temp}°C")

        if weather_dest_desc and weather_dest_temp:
            st.markdown(f"## Weather at {destination}:")
            st.write(f"Weather: {weather_dest_desc}")
            st.write(f"Temperature: {weather_dest_temp}°C")

        st.markdown(f"## Hotels near {origin}:")
        st.write(", ".join(hotels_origin))

        st.markdown(f"## Restaurants near {origin}:")
        st.write(", ".join(restaurants_origin))

        st.markdown(f"## Hotels near {destination}:")
        st.write(", ".join(hotels_destination))

        st.markdown(f"## Restaurants near {destination}:")
        st.write(", ".join(restaurants_destination))
    else:
        st.error("Please enter both origin and destination locations.")
