from utils.api_key import API_KEY
from utils.api_forecast_to_csv import yeet_the_weather_data
import requests

# Run this with:
# python -m utils.api_utils or main.py


def did_my_key_make_it():
    print(f'Here is the key {API_KEY}')


# The key can be printed to the console with:
# did_my_key_make_it()

def city_to_search():
    city = input("What city do you want to weather data for? ")
    print(f"Okay, we will search for weather in {city}.")
    return city

# handy helper function!

# use .get bc it helps with unpredictable of optional API data. If the key doesn't exist, returns None, helps to avoid KeyErrors.


def hold_weather_data(data):
    return {
        "city": data.get("name"),
        "temperature": data["main"].get("temp"),
        "description": data["weather"][0].get("description"),
        "feels_like": data["main"].get("feels_like"),
        "wind_speed": data["wind"].get("speed"),
        "coordinates": (data["coord"]["lat"], data["coord"]["lon"])
    }


def get_the_weather_data(city):
    get_lat_lon_url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}'
    # get the status code response, will it fail?!
    lat_lon_response = requests.get(get_lat_lon_url)
    # lat-long-data is the weather response.json() a WALL of info to wade through
    lat_lon_data = lat_lon_response.json()

    # handle the possible API problems....
    if not lat_lon_data:
        print("City not found, sorry! ")
        return

    latitude = lat_lon_data[0]["lat"]
    longitude = lat_lon_data[0]["lon"]

    weather_data_url = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}&units=imperial'
    # get the status code response, will it fail?!
    weather_res = requests.get(weather_data_url)
    # weather_res.json() is the actual weather data to sift through!
    # verify that's what it is with:
    # print(weather_res.json(), 'weather res.json()')
    weather_data_for_city = weather_res.json()

    weather_info = hold_weather_data(weather_data_for_city)

    print(f"""Current weather in {weather_info['city']} is:
          Temperature: {weather_info['temperature']}
          Current Conditions: {weather_info['description']}
          Feels like: {weather_info['feels_like']}
          Wind speed: {weather_info['wind_speed']} MPH
          Latitude and Longitude of {weather_info['city']} is {weather_info['coordinates']}
          """)
