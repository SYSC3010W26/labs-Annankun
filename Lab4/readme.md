```markdown
# Lab 4 - Traffic Light Control

## Deliverables

### Fritzing Diagrams
- [Modified Breadboard View](./modify_Breadboard.png) - Resolved GPIO conflict
- [Modified Schematic View](./modify_Schematic.png) - Resolved GPIO conflict
- [RPi4 I2C Sensor Breadboard](./Rpi4_breadboard.png) - I2C sensor circuit

### Circuit Photo
- [Crosswalk Circuit](./crosswalk_circuit.png)

### Scripts
- [traffic_lights.py](./traffic_lights.py) - TrafficLights class
- [traffic_lights_test.py](./traffic_lights_test.py) - Unit tests
- [crosswalk_simulation.py](./crosswalk_simulation.py) - Crosswalk simulation

### Team Mini-Project
- [Lab4 Mini-Project](https://github.com/SYSC3010W26/lab4-groupwork-l1_g3)

## How to Run

```bash
sudo python3 traffic_lights_test.py
sudo python3 crosswalk_simulation.py
```

## GPIO Pins

- Red LED: GPIO 12
- Yellow LED: GPIO 5
- Green LED: GPIO 24
- Button: GPIO 17
```