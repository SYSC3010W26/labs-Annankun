# -----------------------------
# Imports
# -----------------------------
from flask import Flask, render_template                 # Flask web framework + render HTML templates
from flask_socketio import SocketIO, emit                # SocketIO for websocket events and emitting messages
import json                                               # Encode/decode JSON strings

from sense_hat import SenseHat                            # SenseHAT library to control the 8x8 LED matrix

# -----------------------------
# Global state: LED colors
# -----------------------------
# A list of 64 pixels, each pixel is [R, G, B].
# Initialize all LEDs to a dim gray so the grid is visible at start.
colors = [[10, 10, 10] for _ in range(64)]

# -----------------------------
# SenseHAT setup
# -----------------------------
sense = SenseHat()                                        # Create SenseHAT object
sense.clear()                                             # Clear physical LEDs at program start

# -----------------------------
# Flask + SocketIO setup
# -----------------------------
app = Flask(__name__)                                     # Create Flask app
app.config["SECRET_KEY"] = "secret!"                      # Secret key needed by Flask-SocketIO sessions

socketio = SocketIO(app)                                  # Bind SocketIO to the Flask app (websocket server)

# -----------------------------
# Helper functions
# -----------------------------
def hex_to_rgb_color(color: str):
    """
    Convert a HEX color string like '#00ff00' to [0, 255, 0].
    The webpage uses HEX strings, but SenseHAT uses integer RGB values.
    """
    color = color.strip("#")                               # Remove leading '#'
    rgb = [int(color[i:i+2], 16) for i in (0, 2, 4)]       # Convert each 2-hex-digit component to int
    return rgb

def sync_sensehat():
    """
    Push the 'colors' array (64 RGB pixels) to the physical SenseHAT LED matrix.
    """
    sense.set_pixels(colors)                                # Set all 64 LEDs at once

# -----------------------------
# Flask route: serve the GUI page
# -----------------------------
@app.route("/")
def index():
    """
    Render the HTML page (must be located inside templates/ folder).
    """
    return render_template("Lab3-Colour-Picker.html")

# -----------------------------
# SocketIO events
# -----------------------------
@socketio.on("connect")
def send_led_colors():
    """
    This runs when a browser first connects to the server.
    We send the current colors so the webpage LED grid matches the server state.
    """
    # Send the full 64-color list to the new client only
    emit("current_colors", json.dumps(dict(colors=colors)))

@socketio.on("update_led")
def update_led_color(data):
    """
    This runs when the webpage sends an 'update_led' websocket event.
    Example incoming data:
        {"id":"59","color":"#0000ff"}
    Steps:
      1) Update server-side color array
      2) Update the physical SenseHAT LEDs
      3) Broadcast update to all connected clients so everyone stays in sync
    """
    data = json.loads(data)                                # Decode JSON string to Python dict

    led_id = int(data["id"])                               # Which LED index (0..63)
    rgb = hex_to_rgb_color(data["color"])                  # Convert HEX string to [R,G,B]

    colors[led_id] = rgb                                   # Update server-side state
    sync_sensehat()                                        # Update physical SenseHAT to match state

    # Broadcast the update to ALL connected browsers (including the one that clicked)
    emit(
        "update_led",
        json.dumps(dict(id=data["id"], color=data["color"])),
        broadcast=True
    )

@socketio.on("clear_leds")
def clear_leds():
    """
    This runs when the user clicks the 'Clear LEDs' button on the webpage.
    Steps:
      1) Set all server-side colors to black
      2) Clear the physical SenseHAT display
      3) Broadcast a 'clear_leds' event so all clients clear their GUI grid
    """
    for i in range(64):
        colors[i] = [0, 0, 0]                              # Black/off for every LED

    sense.clear()                                          # Clear the physical SenseHAT LEDs

    emit("clear_leds", broadcast=True)                     # Tell all browsers to clear their GUI

# -----------------------------
# Start server
# -----------------------------
if __name__ == "__main__":
    # host="0.0.0.0" allows other devices on the same Wi-Fi to access it using RPi IP address
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
