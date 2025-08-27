import math
import smbus2
import drivers.is_raspberry

from drivers.SingletonPeripherals import SingletonPeripherals as SP

if drivers.is_raspberry.it_is():
    import RPi.GPIO as GPIO


def run(az: float, alt: float) -> None:
    def mpu6050_data() -> tuple[float, float, float] | None:
        def start_restart():
            bus = smbus2.SMBus(1)
            bus.write_byte_data(SP().MPU6050_ADDR, SP().PWR_MGMT_1, 0)
            return bus

        def read_raw_data(bus, addr):
            high = bus.read_byte_data(SP().MPU6050_ADDR, addr)
            low = bus.read_byte_data(SP().MPU6050_ADDR, addr + 1)
            value = (high << 8) | low
            if value > 32767:
                value -= 65536
            return value

        if not SP().mpu6050_bus:
            SP().mpu6050_bus = start_restart()
        try:
            accel_x = read_raw_data(SP().mpu6050_bus, SP().ACCEL_XOUT_H)
            accel_y = read_raw_data(SP().mpu6050_bus, SP().ACCEL_XOUT_H + 2)
            accel_z = read_raw_data(SP().mpu6050_bus, SP().ACCEL_XOUT_H + 4)
            accel_x /= 16384.0 / 9.81
            accel_y /= 16384.0 / 9.81
            accel_z /= 16384.0 / 9.81

            a = math.sqrt(accel_x**2 + accel_y**2 + accel_z**2)
            if a == 0:
                return None

            thetaX = math.degrees(math.acos(accel_x / a))
            thetaY = math.degrees(math.acos(accel_y / a))
            thetaZ = math.degrees(math.acos(accel_z / a))
            return thetaX, thetaY, thetaZ
        except:
            SP().mpu6050_bus = None
            mpu6050_data()

    def forward_azimuth(speed):
        GPIO.output(SP().IN1, GPIO.HIGH)
        GPIO.output(SP().IN2, GPIO.LOW)
        SP().pwm_a.value = speed

    def backward_azimuth(speed):
        GPIO.output(SP().IN1, GPIO.LOW)
        GPIO.output(SP().IN2, GPIO.HIGH)
        SP().pwm_a.value = speed

    def forward_altitude(speed):
        GPIO.output(SP().IN3, GPIO.HIGH)
        GPIO.output(SP().IN4, GPIO.LOW)
        SP().pwm_b.value = speed

    def backward_altitude(speed):
        GPIO.output(SP().IN3, GPIO.LOW)
        GPIO.output(SP().IN4, GPIO.HIGH)
        SP().pwm_b.value = speed

    def stop_azimuth():
        GPIO.output(SP().IN1, GPIO.LOW)
        GPIO.output(SP().IN2, GPIO.LOW)
        SP().pwm_a.value = 0

    def stop_altitude():
        GPIO.output(SP().IN3, GPIO.LOW)
        GPIO.output(SP().IN4, GPIO.LOW)
        SP().pwm_b.value = 0

    def get_az() -> float:
        return SP().rotary_encoder.steps

    def get_alt() -> float:
        return mpu6050_data()[0]

    az_real = get_az()
    alt_real = get_alt()
    print(f"Target {az:05f}, {alt:05f}", end="\t")
    print(f"Position {az_real:05f}. {alt_real:05f}", end="\t")
    ang_res = 5

    if az > az_real + ang_res:
        forward_azimuth(1)
        print("→", end=" ")
    elif az < az_real - ang_res:
        backward_azimuth(1)
        print("←", end=" ")
    else:
        stop_azimuth()
        print("↔", end=" ")

    if alt > alt_real + ang_res:
        forward_altitude(1)
        print("↑")
    elif alt < alt_real - ang_res:
        backward_altitude(1)
        print("↓")
    else:
        stop_altitude()
        print("↕")
