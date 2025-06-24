import requests
from utils.api_key import API_KEY
from utils.api_forecast_to_csv import yeet_the_weather_data

# Run this with  python -m utils.api_filter bc it's a module :)


def is_it_hot_in_the_city(city):
    open_weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial"
    # get the status code res:
    res = requests.get(open_weather_url)
    if res.status_code != 200:
        print(
            f"Open weather request returned an HTTP status code of {res.status_code}")
        return None
    # the weather data!
    data = res.json()
    # print(f"This is main from the api_filter file {data["main"]}")
    return data["main"]["temp"]


def filter_the_cities(input_temp):
    list_of_cities = [
        "Orlando", "Miami", "Raleigh", "Seattle", "Memphis", "Columbus", "Milwaukee", "Albany", "Tulsa", "Jackson", "Cleveland", "Holden Beach", "Lexington", "Minneapolis", "Boise", "Denver", "Joplin", "Amarillo", "Tucson"
    ]

    print(
        f"Please wait while I search for cities with a temperature above {input_temp}")

    cities_that_match_input = []

    for city in list_of_cities:
        current_temperature = is_it_hot_in_the_city(city)
        if current_temperature is None:
            continue
        if current_temperature >= input_temp:
            cities_that_match_input.append((city, round(current_temperature)))

    return cities_that_match_input

# calling this bad boy main again. it's the main part of my code I want to run :)


def main():
    try:
        input_temp = float(input(
            "Please enter a temperature to check what cities are at or above that value: ")).__round__()
    except ValueError:
        print("Geez, try again with a valid number please! ")
        return

    valid_ciites = filter_the_cities(input_temp)

    if not valid_ciites:
        print("Did not find any cities with temperatures that high! ")
        return

    print("Cities that match your vibe: ")
    for city, current_temperature in valid_ciites:
        print(f"{city}- {current_temperature}*F")

    # my sanity check debuggin:
    # print("DEBUG: ", valid_ciites)

    yeet_the_weather_data(valid_ciites)


if __name__ == "__main__":
    main()
