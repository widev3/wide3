#!/usr/bin/env python3
import time
import busio
from board import SCL, SDA
from flask import Flask, request, jsonify
from adafruit_pca9685 import PCA9685

# =============================
# CONFIGURAZIONE BASE
# =============================
MOTOR_CHANNELS = {"motor1": 0, "motor2": 1}  # Pan  # Tilt

MIN_PULSE = 500  # µs
MAX_PULSE = 2500  # µs
FREQ = 50  # Hz

# =============================
# INIZIALIZZAZIONE PCA9685
# =============================
i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c)
pca.frequency = FREQ


def angle_to_pwm(angle):
    """Converte un angolo (0–180°) in impulso PWM"""
    return int(MIN_PULSE + (angle / 180.0) * (MAX_PULSE - MIN_PULSE))


def move_motor(name, angle):
    """Muove un motore specificato a un certo angolo"""
    if name not in MOTOR_CHANNELS:
        return f"Motore '{name}' non trovato."
    if not (0 <= angle <= 180):
        return f"Angolo fuori range (0–180): {angle}"

    pulse = angle_to_pwm(angle)
    duty = int(pulse / 1000000 * FREQ * 65535)
    pca.channels[MOTOR_CHANNELS[name]].duty_cycle = duty
    return f"{name} → {angle}° ({pulse} µs)"


# =============================
# SERVER FLASK
# =============================
app = Flask(__name__)


@app.route("/move")
def move():
    name = request.args.get("motor")
    angle = request.args.get("angle", type=float)
    if not name or angle is None:
        return jsonify({"error": "Parametri mancanti: motor e angle"}), 400
    result = move_motor(name, angle)
    return jsonify({"status": "ok", "message": result})


@app.route("/")
def index():
    return """
    <h2>Controllo Motori PCA9685</h2>
    <form action="/move">
      <label>Motore:</label>
      <select name="motor">
        <option value="motor1">motor1</option>
        <option value="motor2">motor2</option>
      </select><br><br>
      <label>Angolo (0–180):</label>
      <input type="number" name="angle" min="0" max="180"><br><br>
      <input type="submit" value="Muovi">
    </form>
    """


if __name__ == "__main__":
    print("Server locale attivo su http://localhost:5000")
    app.run(host="0.0.0.0", port=5000)
