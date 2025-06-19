from utils.api_key import API_KEY
from datetime import datetime
from utils.api_forecast_to_csv import yeet_the_weather_data
import requests


def did_my_key_make_it():
    print(f'Here is the key {API_KEY}')


# The key can be printed to the console with:
# python -m utils.api_utils
# did_my_key_make_it()

def city_to_search():
    city = input("What city do you want to weather data for? ")
    print(f"Okay, we will search for Weather in {city}.")
    return city


def get_the_weather_data(city):
    get_lat_lon_url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}'
    lat_lon_response = requests.get(get_lat_lon_url)
    lat_lon_data = lat_lon_response.json()

    if not lat_lon_data:
        print("City not found, sorry! ")
        return

    latitude = lat_lon_data[0]["lat"]
    longitude = lat_lon_data[0]["lon"]
    geolocation_data = (latitude, longitude)

    weather_data_url = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}&units=imperial'
    weather_res = requests.get(weather_data_url)
    weather_data_for_city = weather_res.json()
    print(weather_data_for_city)

    weather_info = hold_weather_data(weather_data_for_city)
    forecast_info = forecast(geolocation_data, weather_info['city'])

    print(f"""Current weather in {weather_info['city']} is:
          Temperature: {weather_info['temperature']} F
          Current Conditions: {weather_info['description']}
          Feels like: {weather_info['feels_like']}
          Wind speed: {weather_info['wind_speed']} MPH
          Latitude and Longitude of {weather_info['city']} is {weather_info['coordinates']}
          """)

    yeet_the_weather_data(forecast_info, weather_info["city"])


def hold_weather_data(data):
    return {
        "city": data.get("name"),
        "temperature": data["main"].get("temp"),
        "description": data["weather"][0].get("description"),
        "feels_like": data["main"].get("feels_like"),
        "wind_speed": data["wind"].get("speed"),
        "coordinates": (data["coord"]["lat"], data["coord"]["lon"])
    }


def forecast(my_fancy_tuple, city):
    # unpack my tuple:
    lat, lon = my_fancy_tuple
    forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}&units=imperial"
    response = requests.get(forecast_url)
    if response.status_code != 200:
        print(
            f"OpenWeatherAPI request failed with status code {response.status_code}")
        return []
    forecast_res = response.json()

    print("Keys in forecast response: ", forecast_res.keys())

    forecast_info = []
    for day in forecast_res.get("list", [])[:5]:
        ugly_date = day["dt_txt"]
        date_to_strip = datetime.strptime(ugly_date, "%Y-%m-%d %H:%M:%S")
        day_and_time = date_to_strip.strftime("%B %d at %I %p")

        temp = day["main"]["temp"]
        description = day["weather"][0]["description"]

        forecast_info.append({
            "dayandtime": day_and_time,
            "temperature": temp,
            "description": description
        })

    print(f"\nOpenWeather 3 Hour Futurecast for {city}: \n")
    for forecast in forecast_info:
        print(
            f"{forecast['dayandtime']}: {forecast['description'].capitalize()} -  {round(forecast['temperature'])}")
    return forecast_info
