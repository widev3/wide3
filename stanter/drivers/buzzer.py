from time import sleep
import drivers.SingletonPeripherals as sp


def play(tune):
    for note, duration in tune:
        tb.play(note)
        sleep(duration)
    tb.stop()
