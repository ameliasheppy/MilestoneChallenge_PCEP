from utils.api_key import API_KEY
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

    weather_data_url = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}&units=imperial'
    weather_res = requests.get(weather_data_url)
    weather_data_for_city = weather_res.json()
    print(weather_data_for_city)

    print(f"""Current weather in {weather_data_for_city['name']} is:
          Temperature: {weather_data_for_city['main']['temp']} F
          Current Conditions: {weather_data_for_city['weather'][0]['description']}
          Feels like: {weather_data_for_city['main']['feels_like']}
          """)
