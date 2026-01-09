from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

while True:
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()

    msg = f"T:{t:.1f}C P:{p:.0f}hPa H:{h:.0f}%"
    sense.show_message(msg, scroll_speed=0.35)

    sleep(1)


