import time
from traffic_lights import TrafficLights
from gpiozero import Device, Button

class CrosswalkSimulation:
    """Pedestrian crosswalk simulation - traffic light with button control"""
    
    def __init__(self, red_pin=12, yellow_pin=5, green_pin=24, button_pin=17):
        """Initialize traffic light and button
        
        Args:
            red_pin: GPIO pin for red light
            yellow_pin: GPIO pin for yellow light
            green_pin: GPIO pin for green light
            button_pin: GPIO pin for button
        """
        self.traffic = TrafficLights(red_pin, yellow_pin, green_pin)
        self.button = Button(button_pin)
        self.state = "red"
    
    def run(self):
        """Run the traffic light simulation"""
        try:
            print("🚦 Traffic light simulation started!")
            print("Red: 5s → Green: 5s → Press button for Yellow: 2s → Red")
            print("\nPress Ctrl+C to stop\n")
            
            while True:
                # Red light 5s
                print("🔴 Red light ON (5 seconds)")
                self.traffic.red()
                self.state = "red"
                time.sleep(5)
                
                # Green light 5s or button press
                print("🟢 Green light ON (5 seconds or press button to skip)")
                self.traffic.green()
                self.state = "green"
                
                button_pressed = self.button.wait_for_press(timeout=5)
                
                if button_pressed:
                    print("👤 Pedestrian pressed button!")
                    self.state = "yellow"
                else:
                    print("⏱️  5 seconds elapsed, switching to yellow")
                    self.state = "yellow"
                
                # Yellow light 2s
                print("🟡 Yellow light ON (2 seconds)")
                self.traffic.yellow()
                time.sleep(2)
                
                print("Cycle repeating...\n")
                
        except KeyboardInterrupt:
            print("\n\n⛔ Simulation stopped")
            self.traffic.off()

if __name__ == "__main__":
    simulation = CrosswalkSimulation()
    simulation.run()