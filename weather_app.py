
import requests

API_KEY = input("Enter your OpenWeather API key: ").strip()
CITY = input("Enter city name: ").strip()

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": CITY,
    "appid": API_KEY,
    "units": "metric"
}

try:
    response = requests.get(url, params=params, timeout=10)
    data = response.json()

    if response.status_code == 200:
        print("\n--- Live Weather Report ---")
        print("City:", data["name"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Feels like:", data["main"]["feels_like"], "°C")
        print("Humidity:", data["main"]["humidity"], "%")
        print("Weather:", data["weather"][0]["description"].title())
        print("Wind speed:", data["wind"]["speed"], "m/s")
    else:
        print("Weather API error:", data.get("message", "Unknown error"))

except requests.RequestException as error:
    print("Network error:", error)
except (KeyError, ValueError):
    print("Could not read weather data.")

