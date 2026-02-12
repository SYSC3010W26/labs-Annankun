from traffic_lights import TrafficLights
from gpiozero import LED

def test_traffic_lights():
    """Test all methods of TrafficLights class"""
    
    # Create TrafficLights instance
    traffic = TrafficLights(red_pin=12, yellow_pin=5, green_pin=24)
    
    # Test red()
    traffic.red()
    assert traffic.red_led.is_lit == True, "Red light should be on"
    assert traffic.yellow_led.is_lit == False, "Yellow light should be off"
    assert traffic.green_led.is_lit == False, "Green light should be off"
    print("✅ red() test passed")
    
    # Test yellow()
    traffic.yellow()
    assert traffic.red_led.is_lit == False, "Red light should be off"
    assert traffic.yellow_led.is_lit == True, "Yellow light should be on"
    assert traffic.green_led.is_lit == False, "Green light should be off"
    print("✅ yellow() test passed")
    
    # Test green()
    traffic.green()
    assert traffic.red_led.is_lit == False, "Red light should be off"
    assert traffic.yellow_led.is_lit == False, "Yellow light should be off"
    assert traffic.green_led.is_lit == True, "Green light should be on"
    print("✅ green() test passed")
    
    # Test off()
    traffic.off()
    assert traffic.red_led.is_lit == False, "Red light should be off"
    assert traffic.yellow_led.is_lit == False, "Yellow light should be off"
    assert traffic.green_led.is_lit == False, "Green light should be off"
    print("✅ off() test passed")
    
    print("\n🎉 All tests passed!")

if __name__ == "__main__":
    test_traffic_lights()