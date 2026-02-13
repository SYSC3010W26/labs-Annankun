#!/usr/bin/env python3
"""
Lab2 Database Data Logger
Reads temperature, humidity, and pressure from SenseHAT
and logs data to SQLite database every second
"""

import sqlite3
from sense_hat import SenseHat
import time
from datetime import datetime

DB_NAME = 'sensorDB.db'

def setup_database():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sensordata (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            datetime TEXT NOT NULL,
            temperature REAL,
            humidity REAL,
            pressure REAL
        )
    ''')
    
    conn.commit()
    print(f"Database '{DB_NAME}' and table 'sensordata' ready.")
    return conn, cursor

def log_sensor_data(sense, cursor, conn):

    temperature = sense.get_temperature()
    humidity = sense.get_humidity()
    pressure = sense.get_pressure()
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    

    cursor.execute('''
        INSERT INTO sensordata (datetime, temperature, humidity, pressure)
        VALUES (?, ?, ?, ?)
    ''', (current_time, temperature, humidity, pressure))
    
    conn.commit()
    
=    print(f"[{current_time}] T: {temperature:.2f}°C | H: {humidity:.2f}% | P: {pressure:.2f} mbar")

def main():

    conn, cursor = setup_database()
    

    sense = SenseHat()
    sense.clear() 
    
    print("Starting data logging... Press Ctrl+C to stop.")
    print("-" * 60)
    
    try:
        while True:
            log_sensor_data(sense, cursor, conn)
            time.sleep(1)  
            
    except KeyboardInterrupt:
        print("\n" + "-" * 60)
        print("Data logging stopped.")
        

        cursor.execute('SELECT COUNT(*) FROM sensordata')
        count = cursor.fetchone()[0]
        print(f"Total records logged: {count}")
        
    finally:

        conn.close()
        sense.clear()
        print("Database connection closed.")

if __name__ == '__main__':
    main()