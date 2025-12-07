# 🌦️ Real-Time Weather Detection Application

A Python application that fetches **live weather information** using the OpenWeatherMap API and stores the results in a CSV file for future reference.

## 📁 Project Structure
```
.
├── main.py
├── real.py
└── weather_data.csv   (auto-generated)
```

## 🚀 Features

### ✔️ Live Weather Fetching
Retrieves:
- Temperature
- Feels Like
- Humidity
- Weather Condition
- Wind Speed

### ✔️ User Input
User enters the city name, and the program fetches and stores the weather info.

### ✔️ CSV Logging
Each log entry includes:
- Timestamp
- City
- Country
- Temperature
- Feels Like
- Humidity
- Condition
- Wind Speed

### ✔️ Error Handling
Handles invalid city names or API-related errors gracefully.

## 🧠 How It Works

1. User runs `main.py`.
2. `WeatherApp.run()` asks for a city.
3. `request(city)` fetches data from OpenWeather.
4. `information(city)` prints weather info.
5. `store_weather(city)` logs data into `weather_data.csv`.

## 📦 Requirements

- Python 3.x  
- `requests` library  
- Internet connection  

Install dependencies:
```
pip install requests
```

## ▶️ Running the App

```
python main.py
```

## 📊 Example Output

```
Weather in Hyderabad:
 Temperature: 30°C
 Feels Like: 32°C
 Condition: Clear sky
 Humidity: 40%
 Wind Speed: 3 m/s
```

## 🔧 API Configuration

Set your API key:
```
setx OPENWEATHER_API_KEY your_api_key
```

## 🔮 Future Enhancements
- GUI application  
- Weekly forecast  
- Weather data visualization  
- Auto-scheduled logging  
- Export logs to Excel/PDF  
