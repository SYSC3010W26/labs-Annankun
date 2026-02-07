#!/usr/bin/env python3
"""
Lab2 Database Data Visualizer
Reads sensor data from SQLite database and creates visualization plots
"""

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Database filename
DB_NAME = 'sensorDB.db'

def load_data_from_db():
    """Load data from database into pandas DataFrame"""
    conn = sqlite3.connect(DB_NAME)
    
    # Use pandas to directly read SQL query results
    query = "SELECT * FROM sensordata"
    df = pd.read_sql_query(query, conn)
    
    conn.close()
    
    # Convert datetime column to pandas datetime objects
    df['datetime'] = pd.to_datetime(df['datetime'])
    
    print(f"Loaded {len(df)} records from database")
    return df

def plot_sensor_data(df):
    """Create visualization plot with dual Y-axes"""
    # Create figure
    fig, ax1 = plt.subplots(figsize=(14, 8))
    
    # Set title
    plt.title('Sensor Data Over Time', fontsize=16, fontweight='bold', pad=20)
    
    # Left Y-axis: Temperature and Humidity
    ax1.set_xlabel('Time [%H:%M:%S]', fontsize=12)
    ax1.set_ylabel('Temperature [°C], Humidity [%]', fontsize=12, color='black')
    
    # Plot temperature (blue)
    line1 = ax1.plot(df['datetime'], df['temperature'], 
                     'o-', color='blue', linewidth=2, markersize=4,
                     label='Temperature [°C]', alpha=0.7)
    
    # Plot humidity (green)
    line2 = ax1.plot(df['datetime'], df['humidity'], 
                     'o-', color='green', linewidth=2, markersize=4,
                     label='Humidity [%]', alpha=0.7)
    
    ax1.tick_params(axis='y', labelcolor='black')
    ax1.grid(True, alpha=0.3, linestyle='--')
    
    # Right Y-axis: Pressure
    ax2 = ax1.twinx()
    ax2.set_ylabel('Pressure [millibars]', fontsize=12, color='red')
    
    # Plot pressure (red)
    line3 = ax2.plot(df['datetime'], df['pressure'], 
                     'o-', color='red', linewidth=2, markersize=4,
                     label='Pressure [millibars]', alpha=0.7)
    
    ax2.tick_params(axis='y', labelcolor='red')
    
    # Format X-axis time display
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
    plt.xticks(rotation=45)
    
    # Combine legends
    lines = line1 + line2 + line3
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc='upper right', fontsize=10, framealpha=0.9)
    
    # Adjust layout
    plt.tight_layout()
    
    # Save plot
    output_file = 'lab2-database-plot.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"Plot saved as '{output_file}'")
    
    # Display plot
    plt.show()

def main():
    """Main function"""
    print("Loading data from database...")
    df = load_data_from_db()
    
    # Display data statistics
    print("\nData Summary:")
    print(f"  Temperature: {df['temperature'].min():.2f}°C - {df['temperature'].max():.2f}°C")
    print(f"  Humidity: {df['humidity'].min():.2f}% - {df['humidity'].max():.2f}%")
    print(f"  Pressure: {df['pressure'].min():.2f} - {df['pressure'].max():.2f} mbar")
    print(f"  Time range: {df['datetime'].min()} to {df['datetime'].max()}")
    
    print("\nCreating visualization...")
    plot_sensor_data(df)

if __name__ == '__main__':
    main()