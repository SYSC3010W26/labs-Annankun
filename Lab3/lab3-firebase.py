import pyrebase
import time
from sense_hat import SenseHat

config = {
    "apiKey": "AIzaSyD4gpicXr_4gcQJDr5EGQYfQku47m6bnc0",
    "authDomain": "lab3-d0c9f.firebaseapp.com",
    "databaseURL": "https://lab3-d0c9f-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "lab3-d0c9f",
    "storageBucket": "lab3-d0c9f.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

username = "annanjiang"
sense = SenseHat()

# 写 10 组数据
for _ in range(10):
    ts = str(int(time.time()))

    temp = sense.get_temperature()
    hum = sense.get_humidity()
    pres = sense.get_pressure()

    db.child(username).child("temperature").child(ts).set(temp)
    db.child(username).child("humidity").child(ts).set(hum)
    db.child(username).child("pressure").child(ts).set(pres)

    time.sleep(1)

def print_last3(user):
    for sensor in ["temperature", "humidity", "pressure"]:
        snap = db.child(user).child(sensor).get()
        items = snap.each() or []
        last3 = items[-3:]
        print(f"\n{user} - {sensor} (last 3)")
        for item in last3:
            print(f"  {item.key()} : {item.val()}")

# 先打印你自己的最近3条（确认写入成功）
print_last3("annanjiang")

# 再打印队友的：把下面名字改成你队友的 username
print_last3("A")
# print_last3("teammate2")
