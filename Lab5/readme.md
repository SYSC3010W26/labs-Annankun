# Lab 5 - Computer Vision Mini Project

## Web Streaming (Section 3.4)
Unable to access the web streaming interface despite multiple troubleshooting attempts:
- Successfully installed simplejpeg dependency
- Confirmed server is listening on port 8000
- Tested both localhost and IP address
- No firewall blocking

The mjpeg_server.py script has been modified and is included.

## Mini Project (Section 4.4)
Implemented a home security system with:
- Background image capture with countdown
- Person detection using background subtraction
- SenseHAT LED alarm
- Command line menu interface

### Threshold Value
Experimentally determined threshold: [20000000]
- Based on testing with different lighting conditions
- Balances sensitivity vs. false positives