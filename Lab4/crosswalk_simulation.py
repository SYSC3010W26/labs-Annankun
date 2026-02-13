import time
from traffic_lights import TrafficLights
from gpiozero import Device, Button

class CrosswalkSimulation:
    def __init__(self, red_pin=12, yellow_pin=5, green_pin=24, button_pin=17):
        self.traffic = TrafficLights(red_pin, yellow_pin, green_pin)
        self.button = Button(button_pin)
        self.state = "red"
    
    def run(self):
        try:
            print("Traffic light simulation started!")
            print("Red: 5s -> Green: 5s -> Yellow: 2s -> Red\n")
            
            while True:
                print("Red light ON (5 seconds)")
                self.traffic.red()
                time.sleep(5)
                
                print("Green light ON (5 seconds)")
                self.traffic.green()
                button_pressed = self.button.wait_for_press(timeout=5)
                
                if button_pressed:
                    print("Pedestrian pressed button!")
                
                print("Yellow light ON (2 seconds)")
                self.traffic.yellow()
                time.sleep(2)
                print()
                
        except KeyboardInterrupt:
            print("\nSimulation stopped")
            self.traffic.off()

if __name__ == "__main__":
    simulation = CrosswalkSimulation()
    simulation.run()