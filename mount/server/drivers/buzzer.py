import drivers.is_raspberry

if drivers.is_raspberry.it_is():
    from time import sleep
    from gpiozero import TonalBuzzer

    TBPIN = 4
    tb = TonalBuzzer(TBPIN)


def play(tune):
    for note, duration in tune:
        tb.play(note)
        sleep(duration)
    tb.stop()
