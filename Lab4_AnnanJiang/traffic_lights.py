from gpiozero import LED

class TrafficLights:
    """Traffic light class - controls three LEDs"""
    
    def __init__(self, red_pin, yellow_pin, green_pin):
        """Initialize three LEDs
        
        Args:
            red_pin: GPIO pin for red light
            yellow_pin: GPIO pin for yellow light
            green_pin: GPIO pin for green light
        """
        self.red_led = LED(red_pin)
        self.yellow_led = LED(yellow_pin)
        self.green_led = LED(green_pin)
    
    def red(self):
        """Turn on red light only, turn off others"""
        self.red_led.on()
        self.yellow_led.off()
        self.green_led.off()
    
    def yellow(self):
        """Turn on yellow light only, turn off others"""
        self.red_led.off()
        self.yellow_led.on()
        self.green_led.off()
    
    def green(self):
        """Turn on green light only, turn off others"""
        self.red_led.off()
        self.yellow_led.off()
        self.green_led.on()
    
    def off(self):
        """Turn off all lights"""
        self.red_led.off()
        self.yellow_led.off()
        self.green_led.off()