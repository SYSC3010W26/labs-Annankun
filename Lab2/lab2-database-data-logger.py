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

# 数据库文件名
DB_NAME = 'sensorDB.db'

def setup_database():
    """创建数据库和表结构"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # 创建sensordata表
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
    """读取传感器数据并插入数据库"""
    # 读取传感器数据
    temperature = sense.get_temperature()
    humidity = sense.get_humidity()
    pressure = sense.get_pressure()
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # 插入数据库
    cursor.execute('''
        INSERT INTO sensordata (datetime, temperature, humidity, pressure)
        VALUES (?, ?, ?, ?)
    ''', (current_time, temperature, humidity, pressure))
    
    conn.commit()
    
    # 打印确认信息
    print(f"[{current_time}] T: {temperature:.2f}°C | H: {humidity:.2f}% | P: {pressure:.2f} mbar")

def main():
    """主函数"""
    # 初始化数据库
    conn, cursor = setup_database()
    
    # 初始化SenseHAT
    sense = SenseHat()
    sense.clear()  # 清空LED显示
    
    print("Starting data logging... Press Ctrl+C to stop.")
    print("-" * 60)
    
    try:
        while True:
            log_sensor_data(sense, cursor, conn)
            time.sleep(1)  # 每秒记录一次
            
    except KeyboardInterrupt:
        print("\n" + "-" * 60)
        print("Data logging stopped.")
        
        # 显示统计信息
        cursor.execute('SELECT COUNT(*) FROM sensordata')
        count = cursor.fetchone()[0]
        print(f"Total records logged: {count}")
        
    finally:
        # 关闭数据库连接
        conn.close()
        sense.clear()
        print("Database connection closed.")

if __name__ == '__main__':
    main()