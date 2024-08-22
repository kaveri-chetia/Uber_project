import requests
import pandas as pd
from datetime import datetime, timedelta
import time

# API key for Weatherbit
api_key = 'f383b06faf874e4ea71dddccc7f41371'

# Function to fetch weather data from Weatherbit API
def fetch_weather_data(lat, lon, start_time):
    try:
        # Format the start time in the required format (YYYY-MM-DD:HH)
        start_time_iso = datetime.strptime(start_time, '%Y-%m-%d:%H')
        end_time_iso = start_time_iso + timedelta(hours=1)

        # Format dates back to string for the URL
        start_time_str = start_time_iso.strftime('%Y-%m-%d:%H')
        end_time_str = end_time_iso.strftime('%Y-%m-%d:%H')

        # API request URL
        url = f"https://api.weatherbit.io/v2.0/history/hourly?lat={lat}&lon={lon}&start_date={start_time_str}&end_date={end_time_str}&key={api_key}"

        # Make the request
        response = requests.get(url)
        print(response)
        # Check for a successful response
        if response.status_code == 200:
            data = response.json()
            if 'data' in data and len(data['data']) > 0:
                weather_info = data['data'][0]
                # Extract the desired fields
                return {
                    'precip': weather_info.get('precip', None),
                    'clouds': weather_info.get('clouds', None),
                    'snow': weather_info.get('snow', None),
                    'app_temp': weather_info.get('app_temp', None)
                }
            else:
                print(f"No data available for {lat}, {lon} at {start_time}")
                return None
        elif response.status_code == 429:
            print(f"Rate limit exceeded for {lat}, {lon} at {start_time}. Sleeping for 60 seconds.")
            time.sleep(90)  # Pause for 60 seconds
            return fetch_weather_data(lat, lon, start_time)  # Retry the request
        else:
            print(f"Failed to fetch data for {lat}, {lon} at {start_time}. HTTP Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Load the CSV file containing latitude, longitude, and start time
input_csv = "input.csv"
output_csv = "weather_data_output.csv"

df = pd.read_csv(input_csv)

# Prepare a list to store the results
weather_data = []

# Loop over each row in the input CSV and fetch the weather data
for index, row in df.iterrows():
    lat = row['latitude']
    lon = row['longitude']
    start_time = row['start_time']

    weather_info = fetch_weather_data(lat, lon, start_time)
    if weather_info:
        weather_info['latitude'] = lat
        weather_info['longitude'] = lon
        weather_info['start_time'] = start_time
        weather_data.append(weather_info)

# Convert the weather data into a DataFrame
weather_df = pd.DataFrame(weather_data)

# Save the collected data to a new CSV file
weather_df.to_csv(output_csv, index=False)

print(f"Weather data has been saved to {output_csv}")
