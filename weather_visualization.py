import requests
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Function to get data from OpenWeatherMap API
def get_weather_data(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"  # You can choose units: 'metric' for Celsius
    response = requests.get(complete_url)
    data = response.json()  # Convert response to JSON
    return data

# Function to parse and return relevant weather information
def parse_weather_data(data):
    # Extracting relevant data
    main_data = data.get("main", {})
    weather = data.get("weather", [{}])[0]
    wind = data.get("wind", {})
    
    parsed_data = {
        "city": data.get("name"),
        "temperature": main_data.get("temp"),
        "humidity": main_data.get("humidity"),
        "pressure": main_data.get("pressure"),
        "description": weather.get("description"),
        "wind_speed": wind.get("speed"),
        "wind_direction": wind.get("deg"),
    }
    return parsed_data

# Function to plot visualizations
def plot_weather_data(weather_data):
    # Creating a DataFrame for better visualization
    df = pd.DataFrame([weather_data])
    
    # Temperature and humidity visualization
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    
    sns.barplot(x=["Temperature"], y=[df["temperature"].values[0]], ax=axes[0])
    axes[0].set_title(f"Temperature in {df['city'].values[0]} (°C)")
    
    sns.barplot(x=["Humidity"], y=[df["humidity"].values[0]], ax=axes[1])
    axes[1].set_title(f"Humidity in {df['city'].values[0]} (%)")
    
    plt.tight_layout()
    plt.show()

# Example usage
if __name__ == "__main__":
    # Enter your OpenWeatherMap API key here
    api_key = "your_api_key_here"
    
    # Fetch weather data for a city
    city = "London"  # Change city as needed
    data = get_weather_data(city, api_key)
    
    if data.get("cod") != 200:  # Check for successful API response
        print("Failed to retrieve data")
    else:
        # Parse data and plot visualization
        weather_data = parse_weather_data(data)
        plot_weather_data(weather_data)
