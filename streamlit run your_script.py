import streamlit as st
import requests

# Add Streamlit sidebar
city = st.sidebar.text_input("Enter City", "London")

# Add title
st.title(f"Weather Information for {city}")

# Fetch weather data
api_key = "your_api_key_here"
weather_data = get_weather_data(city, api_key)

if weather_data.get("cod") != 200:
    st.error("City not found or API error.")
else:
    parsed_data = parse_weather_data(weather_data)
    
    # Display the data
    st.write(f"Temperature: {parsed_data['temperature']}°C")
    st.write(f"Humidity: {parsed_data['humidity']}%")
    st.write(f"Pressure: {parsed_data['pressure']} hPa")
    st.write(f"Weather: {parsed_data['description']}")
    st.write(f"Wind Speed: {parsed_data['wind_speed']} m/s")
