import requests
import os
import csv
from datetime import datetime  # important import


# Centralize configuration to avoid duplicate lines
API_KEY = os.environ.get("OPENWEATHER_API_KEY", "4efc678ccdbd3cb455da8478d3aa3d3e")  # OpenWeather API key
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather" #URI for weather data


def request(city: str): # Function to interact with OpenWeatherMap API
    
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
    }
    try:
        resp = requests.get(WEATHER_URL, params=params)  # requesting weather data from OpenWeatherMap API
    except Exception as e:
        print("\n Error:", str(e))
        return None

    if resp.status_code == 200:# Successful response
        return resp.json() # Converting the text response into JSON format
    else:
        print("\n City not found or API error")
    return None


def information(city: str):
    data = request(city)
    if not data:
        return
    # Converting the text response into JSON format already done in helper
    print(f"\nWeather in {city.title()}:")  # show the city name
    print(f" Temperature: {data['main']['temp']}°C")  # show temperature
    print(f" Feels Like: {data['main']['feels_like']}°C")  # show feels like temperature
    print(f" Condition: {data['weather'][0]['description'].capitalize()}")  # show weather condition
    print(f" Humidity: {data['main']['humidity']}%")  # show humidity
    print(f" Wind Speed: {data['wind']['speed']} m/s")  # show wind speed


# Storing Weather data in CSV file
def store_weather(city: str, filename: str = "weather_data.csv"):
    """Fetch weather for `city` using `request` and append a row to `filename`.

    This is a top-level function (no `self`) so it can be imported and
    called from `main.py` as `store_weather(city)`.
    """
    data = request(city)
    if not data:
        return

    city_name = data.get("name", city)
    country = data.get("sys", {}).get("country", "")
    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    condition = data["weather"][0]["description"].capitalize()
    wind_speed = data["wind"]["speed"]

    file_exists = os.path.isfile(filename)
    with open(filename, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(
                [
                    "Timestamp",
                    "City",
                    "Country",
                    "Temperature (°C)",
                    "Feels Like (°C)",
                    "Humidity (%)",
                    "Condition",
                    "Wind Speed (m/s)",
                ]
            )
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow(
            [timestamp, city_name, country, temperature, feels_like, humidity, condition, wind_speed]
        )
    print(f"\n Weather data for {city_name} stored in {filename}")