# Lab 4 - Traffic Light Control

## Overview
Traffic light control system using GPIO pins to control LEDs and a button for a crosswalk simulation.

## Deliverables

### Circuit Diagrams (Fritzing)
- [Breadboard View](./Breadboard_Lab4_bb.png)
- [Schematic View](./Schematic_Lab4_schem.png)

### Circuit Photo
- [Actual Circuit Setup](./crosswalk_circuit.png)

### Scripts
- [traffic_lights.py](./traffic_lights.py) - TrafficLights class that controls red, yellow, and green lights
- [traffic_lights_test.py](./traffic_lights_test.py) - Unit tests to verify all methods work correctly
- [crosswalk_simulation.py](./crosswalk_simulation.py) - Full simulation with button control

### Team Mini-Project
- [Mini-Project Repository](https://github.com/SYSC3010W26/lab4-groupwork-l1_g3)

---

## Hardware Setup

- Red LED: GPIO 12
- Yellow LED: GPIO 5
- Green LED: GPIO 24
- Button: GPIO 17
- Each LED needs a 200Ω resistor

## How to Run
```bash
# Run tests
sudo python3 traffic_lights_test.py

# Run crosswalk simulation
sudo python3 crosswalk_simulation.py
```

## Traffic Light Sequence

1. Red light - 5 seconds
2. Green light - 5 seconds (press button to skip)
3. Yellow light - 2 seconds
4. Back to red light, repeat

Press Ctrl+C to stop the program