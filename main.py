from utils.api_utils import city_to_search, get_the_weather_data


def main():
    city = city_to_search()
    get_the_weather_data(city)


if __name__ == "__main__":
    main()
