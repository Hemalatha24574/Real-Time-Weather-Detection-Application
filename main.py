"""Real-Time Weather Detection  Application"""
# Author: Pabbu Hemalatha
from real import information, store_weather


class WeatherApp:
    """Simple wrapper class to interact with the weather helper functions."""

    def run(self):
        city = input("Enter City: ")  # Get city name from user
        information(city)  # Show weather info
        store_weather(city)  # Store data in CSV


if __name__ == "__main__":
    app = WeatherApp()
    app.run()