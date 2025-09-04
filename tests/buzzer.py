# https://docs.sunfounder.com/projects/umsk/en/latest/05_raspberry_pi/pi_lesson32_passive_buzzer.html

from time import sleep
from gpiozero import TonalBuzzer

tb = TonalBuzzer(4)


def play(tune):
    for note, duration in tune:
        tb.play(note)
        sleep(duration)
    tb.stop()


tune = [
    # Measure 1
    ("C4", 0.25),
    ("E4", 0.25),
    ("G4", 0.25),
    ("C5", 0.25),
    # Measure 2
    ("B4", 0.25),
    ("A4", 0.25),
    ("G4", 0.5),
    # Measure 3
    ("E4", 0.25),
    ("F4", 0.25),
    ("G4", 0.25),
    (None, 0.25),
    # Measure 4
    ("C5", 0.5),
    ("B4", 0.25),
    ("A4", 0.25),
    # # Measure 5
    ("G4", 0.25),
    ("A4", 0.25),
    ("B4", 0.25),
    ("D5", 0.25),
    # Measure 6
    ("C5", 0.5),
]

play(tune)
