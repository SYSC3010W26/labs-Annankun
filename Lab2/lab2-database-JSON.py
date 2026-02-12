#!/usr/bin/env python3
"""
Lab2 Database JSON Integration
Fetches wind speed data from OpenWeatherMap API
Stores data in Winds table and compares with previous readings
"""

from urllib.request import urlopen 
from urllib.parse import urlencode
import json
import sqlite3
from datetime import datetime

apiKey = "a808bbf30202728efca23e099a4eecc7"
DB_NAME = 'sensorDB.db'

def fetch_wind_from_api(city):
    """从OpenWeatherMap API获取风速数据"""
    params = {"q": city, "units": "metric", "APPID": apiKey}
    arguments = urlencode(params)
    
    address = "http://api.openweathermap.org/data/2.5/weather"
    url = address + "?" + arguments
    
    print(f"Requesting data for {city}...")
    
    try:
        webData = urlopen(url)
        results = webData.read().decode('utf-8')
        webData.close()
        
        data = json.loads(results)
        api_wind_speed = data["wind"]["speed"]
        
        return api_wind_speed
    
    except Exception as e:
        print(f"Error fetching data for {city}: {e}")
        return None

def query_previous_wind_from_db(city):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT WindSpeed FROM Winds
        WHERE City = ?
        ORDER BY Date DESC
        LIMIT 1
    ''', (city,))
    
    result = cursor.fetchone()
    conn.close()
    
    return result[0] if result else None

def store_wind_to_db(city, wind_value):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    cursor.execute('''
        INSERT INTO Winds (City, Date, WindSpeed)
        VALUES (?, ?, ?)
    ''', (city, timestamp, wind_value))
    
    conn.commit()
    conn.close()

def report_wind_change(city, current_value, historical_value):
    if historical_value is None:
        print(f"  {city}: First record - Wind Speed: {current_value:.2f} m/s")
    elif current_value > historical_value:
        difference = current_value - historical_value
        print(f"  {city}: Wind Speed INCREASED by {difference:.2f} m/s (from {historical_value:.2f} to {current_value:.2f})")
    elif current_value < historical_value:
        difference = historical_value - current_value
        print(f"  {city}: Wind Speed DECREASED by {difference:.2f} m/s (from {historical_value:.2f} to {current_value:.2f})")
    else:
        print(f"  {city}: Wind Speed SAME - {current_value:.2f} m/s")

def main():
    cities = ["London", "Paris", "Tokyo", "Ottawa"]
    
    print("=" * 60)
    print("Fetching wind speed data from OpenWeatherMap...")
    print("=" * 60)
    
    for city in cities:
        api_wind = fetch_wind_from_api(city)
        
        if api_wind is None:
            continue
        
        db_wind = query_previous_wind_from_db(city)
        
        report_wind_change(city, api_wind, db_wind)
        
        store_wind_to_db(city, api_wind)
    
    print("=" * 60)
    print("Data saved to database!")
    print("=" * 60)

if __name__ == '__main__':
    main()