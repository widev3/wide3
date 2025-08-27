# https://docs.sunfounder.com/projects/umsk/en/latest/05_raspberry_pi/pi_lesson17_rotary_encoder.html


from gpiozero import RotaryEncoder
from time import sleep

encoder = RotaryEncoder(a=14, b=15, wrap=True, max_steps=360)
last_rotary_value = 0

try:
    while True:
        current_rotary_value = encoder.steps
        if last_rotary_value != current_rotary_value:
            print("Result =", current_rotary_value)
            last_rotary_value = current_rotary_value

        sleep(0.01)

except KeyboardInterrupt:
    print("Program terminated")
