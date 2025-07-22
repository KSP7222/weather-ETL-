import requests
import pandas as pd
from datetime import datetime
import sqlite3
API_KEY = "1f15e3d684be326f722323dcbea6ee16"  
CITIES = ["Japan", "china", "hyderabad", "washington", "pune"]
all_data = []  
for city in CITIES:
    print(f"Fetching data for {city}...")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=1f15e3d684be326f722323dcbea6ee16&units=metric"
    response = requests.get(url)
    data = response.json()
    # Clean just the fields we care about
    cleaned_data = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    all_data.append(cleaned_data)
# Create DataFrame
df = pd.DataFrame(all_data)
# Print DataFrame
print("\nCleaned Data:")
print(df)
conn = sqlite3.connect("weather_data.db")
# Save to table
df.to_sql(
    name="weather",
    con=conn,
    if_exists="append",
    index=False
)
conn.close()
print("Data saved to weather_data.db ✅")

