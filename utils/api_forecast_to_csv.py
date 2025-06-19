import csv


def yeet_the_weather_data(forecast_info, city, filename="forecast.csv",):
    fieldnames = ["City", "Day and Time", "Temperature *F", "Description"]

    # The table headers were super ugly. So I am cleaning them up:
    pretty_table = []
    for column in forecast_info:
        pretty_table.append({
            "City": city,
            "Day and Time": column["dayandtime"],
            "Temperature *F": column["temperature"],
            "Description": column["description"]
        })

    # change the write mode to 'w' to overwrite the file each time
    with open(filename, mode='a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for entry in pretty_table:
            writer.writerow(entry)

    print(f"Forecast data exported successfully to {filename}")
