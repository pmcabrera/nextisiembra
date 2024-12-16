import requests
from datetime import datetime

def get_weather():
    # Define the coordinates for Rosario, Santa Fe
    latitude = -32.9468
    longitude = -60.6393
    
    # URL for the Open-Meteo API to fetch current weather and forecast for the next 2 days
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true&daily=temperature_2m_max,temperature_2m_min,weathercode&timezone=America/Argentina/Buenos_Aires"
    
    # Send GET request to the API
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        
        # Get current weather data
        current_weather = data['current_weather']
        temperature = current_weather.get('temperature', "N/A")
        weather_icon = current_weather.get('weathercode', "N/A")
        
        # Map weather code to an icon description (Open-Meteo weather codes)
        weather_icons = {
            0: "Clear sky",
            1: "Mainly clear",
            2: "Partly cloudy",
            3: "Cloudy",
            45: "Fog",
            48: "Depositing rime fog",
            51: "Drizzle",
            53: "Moderate drizzle",
            55: "Heavy drizzle",
            56: "Freezing drizzle",
            57: "Freezing drizzle, heavy",
            61: "Showers of rain",
            63: "Moderate showers of rain",
            65: "Heavy showers of rain",
            66: "Freezing rain",
            67: "Freezing rain, heavy",
            71: "Snow fall",
            73: "Moderate snow fall",
            75: "Heavy snow fall",
            77: "Snow grains",
            80: "Showers of snow",
            81: "Moderate showers of snow",
            82: "Heavy showers of snow",
            85: "Showers of ice pellets",
            86: "Heavy showers of ice pellets",
            95: "Thunderstorms",
            96: "Thunderstorms with light hail",
            99: "Thunderstorms with heavy hail"
        }
        
        icon_description = weather_icons.get(weather_icon, "Unknown")
        
        # Print the current weather
        print(f"Current weather in Rosario, Santa Fe:")
        print(f"Temperature: {temperature}°C")
        print(f"Weather: {icon_description}")
        
        # Get daily forecast for the next 2 days
        daily_forecast = data['daily']
        
        # Loop through the forecast data and print it
        for i in range(3):  # Display the current day and next 2 days
            date = daily_forecast['time'][i]
            max_temp = daily_forecast['temperature_2m_max'][i]
            min_temp = daily_forecast['temperature_2m_min'][i]
            weather_code = daily_forecast['weathercode'][i]
            weather_desc = weather_icons.get(weather_code, "Unknown")
            
            # Convert the date to a human-readable format
            day_name = datetime.strptime(date, '%Y-%m-%d').strftime('%A')
            
            print(f"\n{day_name} ({date}):")
            print(f"Max Temp: {max_temp}°C")
            print(f"Min Temp: {min_temp}°C")
            print(f"Weather: {weather_desc}")
    
    else:
        print("Failed to retrieve weather data")

if __name__ == "__main__":
    get_weather()
