import requests

API_KEY = 'ec5d5ca20903c64cc97551cf656ca961'  # Replace with your OpenWeatherMap API key
CITY = 'Salem'  # You can change this

def fetch_weather_data(city=CITY):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200 or 'main' not in data:
        raise Exception(data.get("message", "Failed to fetch weather data"))

    temp = data['main']['temp']
    RH = data['main']['humidity']
    wind = data['wind']['speed']
    rain = data.get('rain', {}).get('1h', 0.0)

    return temp, RH, wind, rain
