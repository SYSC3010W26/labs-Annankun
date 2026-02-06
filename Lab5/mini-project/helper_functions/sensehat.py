# sensehat.py

from sense_hat import SenseHat
import time

def get_sensehat():
    """
    This function returns a SenseHat instance
    """
    sense = SenseHat()
    return sense


def alarm(sense, flash_time):
    """
    This function takes in a SenseHat instance and the flash_time
    The display on the SenseHat flashes red (1 second on, 1 second off) for the duration of flash_time
    At the end of the flash_time the SenseHat display should be off
    """
    red = (255, 0, 0)
    off = (0, 0, 0)
    
    elapsed_time = 0
    
    while elapsed_time < flash_time:
        sense.clear(red)
        time.sleep(1)
        elapsed_time += 1
        
        if elapsed_time < flash_time:
            sense.clear(off)
            time.sleep(1)
            elapsed_time += 1
    
    sense.clear(off)