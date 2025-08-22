from time import sleep
from gpiozero import OutputDevice, InputDevice


def run(az: float, alt: float) -> None:
    alt_plus = OutputDevice(17)
    alt_minus = OutputDevice(18)
    az_plus = OutputDevice(19)
    az_minus = OutputDevice(20)
    alt_real = InputDevice(15)
    az_real = InputDevice(16)

    if az > az_real:
        az_minus.off()
        az_plus.on()
    elif az < az_real:
        az_plus.off()
        az_minus.on()

    if alt > alt_real:
        alt_minus.off()
        alt_plus.on()
    elif alt < alt_real:
        alt_plus.off()
        alt_minus.on()

    while True:
        sleep(0.5)
        az_real = get_real_az()
        alt_real = get_real_alt()

        if abs(az - az_real) < 1:
            az_minus.off()
            az_plus.off()

        if abs(alt - alt_real) < 1:
            alt_minus.off()
            alt_plus.off()
