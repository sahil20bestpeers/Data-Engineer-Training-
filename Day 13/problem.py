import requests
import pandas as pd
from datetime import datetime
import time


cities = ['Rome','Italy','London'] 
api_key = 'e8aa8ff928f9028b27294ce00aa89c80' 


def fetch_weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

def process_and_save_data():
    all_data = []
    for city in cities:
        data = fetch_weather_data(city)
        for entry in data['list']:
            all_data.append({
                'City': city,
                'Date & Time': entry['dt_txt'],
                'Temperature (°C)': entry['main']['temp'],
                'Weather': entry['weather'][0]['description'],
                'Humidity (%)': entry['main']['humidity'],
                'Wind Speed (m/s)': entry['wind']['speed'],
                'Timestamp': datetime.utcnow()
            })
    df = pd.DataFrame(all_data)
    df.to_csv('weather_data_changed.csv', mode='a', header=False, index=False)

# Main loop to run the script every 3 hours 
while True:
    process_and_save_data()
    print(f"Data fetched and saved at {datetime.utcnow()}")
    time.sleep(10800)  # Sleep for 3 hours (10800 seconds)
    
    

# clickhouse-client -h localhost --user sahil --password '123' --query="INSERT INTO weather_forecast2 FORMAT CSV" < weather_data_cleaned.csv


# 0 */3 * * * /usr/bin/python3 "/home/developer/vs code/every3_hour.py" >> /home/developer/weather_log.txt 2>&1



# crontab -e
# Add your cron line like:

# bash
# Copy code
# 0 */3 * * * /usr/bin/python3 "/home/developer/Desktop/test/problem.py" >> /home/developer/weather_log.txt 2>&1
# Save and exit the editor.

# Confirm cron is set:

# bash
# Copy code
# crontab -l

