import csv
import os


def yeet_the_weather_data(valid_ciites, filename="forecast.csv",):
    output_dir = "data"
    filepath = os.path.join(output_dir, filename)
    fieldnames = ["City", "Temperature"]

    if not valid_ciites:
        print("No cities to write")
        return

    os.makedirs(output_dir, exist_ok=True)

    file_exists = os.path.isfile(filepath)
    rows = [{"City": city, "Temperature": temperature}
            for city, temperature in valid_ciites]
    # change the write mode to 'a' to append to the file each time
    with open(filepath, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writeheader()
        writer.writerows(rows)
