from utils.api_utils import city_to_search, get_the_weather_data

# the script's main starting point, so I can run it directly!


def main():
    # I am going to pull the value from my city_to_search function we'll see soon
    city = city_to_search()
    # this will make the API request to fetch the weather and do schtuff with it
    get_the_weather_data(city)


# this is the main entry point of my program!
if __name__ == "__main__":
    main()
