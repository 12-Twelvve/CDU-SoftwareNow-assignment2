import pandas as pd
import glob
import os

def create_file(value, path):
    # creates a text file
    directory = os.path.dirname(path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
        print(f"directory created at {directory}")

    with open(path, 'w') as file:
        file.write(value)
        print("File created.!")

def ses_avg(df):
    # Calculate the average temperature for each season across ALL
    # stations and ALL years. Save the results to "average_temp.txt".

    # Aus Session Map
    maps = {
        "Summer": ["December", "January", "February"],
        "Autumn": ["March", "April", "May"],
        "Winter": ["June", "July", "August"],
        "Spring": ["September", "October", "November"]
    }
    season_avgs = {}
    for season, months in maps.items():
        season_avgs[season] = df[months].mean().mean() # initially calculates avg of the months then calculates avg of season

    # result
    result = f"Summer: {round(season_avgs["Summer"], 2)}°C\nAutumn: {round(season_avgs["Autumn"], 2)}°C\nWinter: {round(season_avgs["Winter"], 2)}°C\nSpring: {round(season_avgs["Spring"], 2)}°C\n"
    create_file(str(result), "./results/avg_temperature.txt")

def temp_range():
    # Find the station(s) with the largest temperature range (difference
    # between the highest and lowest temperature ever recorded at that station). Save the
    # results to "largest_temp_range_station.txt".
    print("here in the temperature average")


def temp_stability():
    # Find which station(s) have the most stable temperatures
    # (smallest standard deviation) and which have the most variable temperatures (largest
    # standard deviation). Save the results to "temperature_stability_stations.txt".
    print("here in the temperature stability")



if __name__ =="__main__":
    path = "./temperatures"
    all_files = glob.glob(os.path.join(path, "*.csv"))
    df = []
    for index, file in enumerate(all_files):
        data = pd.read_csv(file)
        file_row = data.shape[0]
        # print(f"{file_row} rows  of file {index}")
        df.append(data)
    actual_df = pd.concat(df, ignore_index=True)

    # total_rows = actual_df.shape[0]
    # print("total rows: ",total_rows)

    # print(actual_df.head())
    # functions calls
    sessional_avg = ses_avg(actual_df)
    # temperature_range = temp_range()
    # temp_stability = temp_stability()
