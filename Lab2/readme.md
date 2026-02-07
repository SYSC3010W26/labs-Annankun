# Lab 2: Databases

This lab explores SQLite databases and data visualization using Python on Raspberry Pi with SenseHAT sensors.

## Files

- `lab2-database-data-logger.py` - Reads temperature, humidity, and pressure from SenseHAT sensors and logs data to SQLite database every second
- `lab2-database-data-visualizer.py` - Reads sensor data from database and creates visualization plots
- `lab2-database-plot.png` - Screenshot of the visualized sensor data
- `lab2-database-manager.png` - Screenshot of the database viewed in SQLite Browser
- `sensorDB.db` - SQLite database containing sensor readings

## Exercise Summaries

### Exercise 1: SQLite Command Line
Learned basic SQLite commands using the command-line interface to create tables, insert data, and query data.

### Exercise 2: Database Manager GUI
Used DB Browser for SQLite to visually manage databases and view table structures.

### Exercise 3: Python Database Logger
Created a Python script that automatically reads SenseHAT sensor data and logs it to an SQLite database.

### Exercise 4: Data Visualization
Used pandas and matplotlib to visualize temperature, humidity, and pressure data over time.

## How to Run

### Data Logger
```bash