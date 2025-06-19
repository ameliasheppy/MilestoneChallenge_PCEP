import csv
import os


def yeet_the_weather_data(filtered_cities, filename="forecast.csv",):
    output_dir = "data"
    filepath = os.path.join(output_dir, filename)
    fieldnames = ["City", "Temperature *F"]

    # The table headers were super ugly. So I am cleaning them up:
    pretty_table = []
    for city, temp in filtered_cities:
        pretty_table.append({
            "City": city,
            "Temperature *F": temp,
        })

    # change the write mode to 'w' to overwrite the file each time
    with open(filepath, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for entry in pretty_table:
            writer.writerow(entry)

    print(f"Forecast data exported successfully to {filepath}")
