# https://projects.raspberrypi.org/en/projects/physical-computing/13
# https://www.hackster.io/ryanchan/how-to-use-the-l298n-motor-driver-b124c5

import time
import RPi.GPIO as GPIO
from gpiozero import PWMLED

ENA = 18
IN1 = 23
IN2 = 24

ENA = 12
IN1 = 8
IN2 = 25

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pwm = PWMLED(ENA)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)


def forward(speed=1):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    pwm.value = speed


def backward(speed=1):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    pwm.value = speed


def stop():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    pwm.value = 0


try:
    forward(0.1)
    backward(0.2)
    forward(0.3)
    backward(0.4)
    forward(0.5)
    backward(0.6)
    forward(0.7)
    backward(0.8)
    forward(0.9)
    backward(1)

    print("Motor stopped.")
    stop()
    time.sleep(2)
except KeyboardInterrupt:
    print("Program interrupted")
finally:
    GPIO.cleanup()
