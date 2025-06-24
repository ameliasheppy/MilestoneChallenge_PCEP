import csv
import os

# take in a list of tuples from the weather result and set the default filename


def yeet_the_weather_data(valid_ciites, filename="forecast.csv",):
    # save the CSV in a folder called data
    output_dir = "data"
    # join data with the filename to create the full path
    filepath = os.path.join(output_dir, filename)
    # set the column headers
    fieldnames = ["City", "Temperature"]

    # if the valid cities is empty, it is handled
    if not valid_ciites:
        print("No cities to write")
        return

    # make sure the data folder exists. if it does, it won't create it again
    os.makedirs(output_dir, exist_ok=True)

    # format my data. Take the list of tuples and turn it to a list of dicts so the csv.DictWriter  won't complain:
    rows = [{"City": city, "Temperature": temperature}
            for city, temperature in valid_ciites]
    # change the write mode to 'a' to append to the file each time
    with open(filepath, mode='w', newline='', encoding='utf-8') as csvfile:
        # write the headers! (City and Temperature from fieldnames)
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # write the headers!
        writer.writeheader()
        # write all the rows to the file!
        writer.writerows(rows)
