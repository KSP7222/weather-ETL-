import requests
import pandas as pd
from datetime import datetime
import sqlite3
import schedule
import time
API_KEY = "1f15e3d684be326f722323dcbea6ee16"  
CITIES = ["Japan", "china", "hyderabad", "washington", "pune"]
def fetch_and_save():
    all_data = []  
    for city in CITIES:
        print(f"Fetching data for {city}...")
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=1f15e3d684be326f722323dcbea6ee16&units=metric"
        response = requests.get(url)
        data = response.json()
        cleaned_data = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        all_data.append(cleaned_data)

    df = pd.DataFrame(all_data)
    print("\nCleaned Data:")
    print(df)# prints the data frame 

    conn = sqlite3.connect("weather_data.db")
    df.to_sql(name="weather", con=conn, if_exists="append", index=False)
    conn.close()#connection is closed 
    print("Data saved to weather_data.db ✅\n")

schedule.every(1).hour.do(fetch_and_save)
print("Scheduler started. Press Ctrl+C to stop.")
fetch_and_save()  # run immediately once

while True:
    schedule.run_pending()
    time.sleep(1)#looks at the code once every second

