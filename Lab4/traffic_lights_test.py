from traffic_lights import TrafficLights

def test_traffic_lights():
    traffic = TrafficLights(red_pin=12, yellow_pin=5, green_pin=24)
    
    traffic.red()
    assert traffic.red_led.is_lit == True
    assert traffic.yellow_led.is_lit == False
    assert traffic.green_led.is_lit == False
    print("red() test passed")
    
    traffic.yellow()
    assert traffic.red_led.is_lit == False
    assert traffic.yellow_led.is_lit == True
    assert traffic.green_led.is_lit == False
    print("yellow() test passed")
    
    traffic.green()
    assert traffic.red_led.is_lit == False
    assert traffic.yellow_led.is_lit == False
    assert traffic.green_led.is_lit == True
    print("green() test passed")
    
    traffic.off()
    assert traffic.red_led.is_lit == False
    assert traffic.yellow_led.is_lit == False
    assert traffic.green_led.is_lit == False
    print("off() test passed")
    
    print("All tests passed!")

if __name__ == "__main__":
    test_traffic_lights()