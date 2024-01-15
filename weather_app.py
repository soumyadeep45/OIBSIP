# Weather report of a city.

import requests

class WeatherApp:

    def __init__(self, api_key):
        self.api_key = api_key

    def get_weather(self, city):
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {"q": city, "appid": self.api_key, "units": "metric"}
        response = requests.get(base_url, params=params)
        return response.json() if response.status_code == 200 else None

    def display_weather(self, weather_data):
        if weather_data:
            main_info = weather_data["main"]
            weather_info = weather_data["weather"][0]

            print(f"\nWeather in- {weather_data['name']}, {weather_data['sys']['country']}:")
            print(f"Description: {weather_info['description']}")
            print(f"Temperature: {main_info['temp']}°C")
            print(f"Humidity: {main_info['humidity']}%")
            print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
        else:
            print("Error: Unable to produce weather report.")

if __name__ == "__main__":
    api_key = "7d71b1bfb00d8b6667d432476440b3d4"

    weather_app = WeatherApp(api_key)

    print("   WELCOME TO THE WEATHER APP")
    city_name = input("Enter the city name: ")

    weather_data = weather_app.get_weather(city_name)
    weather_app.display_weather(weather_data)
    
