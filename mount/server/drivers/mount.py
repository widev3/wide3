import drivers.is_raspberry

if drivers.is_raspberry.it_is():
    import math
    import smbus2
    import RPi.GPIO as GPIO
    from gpiozero import PWMLED
    from gpiozero import RotaryEncoder

    # i2c busses
    MPU6050_ADDR = 0x68
    PWR_MGMT_1 = 0x6B
    ACCEL_XOUT_H = 0x3B
    GYRO_XOUT_H = 0x43
    mpu6050_bus = None

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # azimuth motor
    ENA = 18
    IN1 = 23
    IN2 = 24
    pwm_a = PWMLED(ENA)
    GPIO.setup(IN1, GPIO.OUT)
    GPIO.setup(IN2, GPIO.OUT)

    # altitude motor
    ENB = 12
    IN3 = 8
    IN4 = 25
    pwm_b = PWMLED(ENB)
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT)

    # encoder
    PINA = 14
    PINB = 15
    rotary_encoder = RotaryEncoder(a=PINA, b=PINB, wrap=True, max_steps=360)


def run(az: float, alt: float) -> None:
    def mpu6050_data() -> tuple[float, float, float] | None:
        def start_restart():
            bus = smbus2.SMBus(1)
            bus.write_byte_data(MPU6050_ADDR, PWR_MGMT_1, 0)
            return bus

        def read_raw_data(bus, addr):
            high = bus.read_byte_data(MPU6050_ADDR, addr)
            low = bus.read_byte_data(MPU6050_ADDR, addr + 1)
            value = (high << 8) | low
            if value > 32767:
                value -= 65536
            return value

        if not mpu6050_bus:
            mpu6050_bus = start_restart()
        try:
            accel_x = read_raw_data(mpu6050_bus, ACCEL_XOUT_H)
            accel_y = read_raw_data(mpu6050_bus, ACCEL_XOUT_H + 2)
            accel_z = read_raw_data(mpu6050_bus, ACCEL_XOUT_H + 4)
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
            mpu6050_bus = None
            mpu6050_data()

    def forward_azimuth(speed):
        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.LOW)
        pwm_a.value = speed

    def backward_azimuth(speed):
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.HIGH)
        pwm_a.value = speed

    def forward_altitude(speed):
        GPIO.output(IN3, GPIO.HIGH)
        GPIO.output(IN4, GPIO.LOW)
        pwm_b.value = speed

    def backward_altitude(speed):
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.HIGH)
        pwm_b.value = speed

    def stop_azimuth():
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.LOW)
        pwm_a.value = 0

    def stop_altitude():
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.LOW)
        pwm_b.value = 0

    def get_az() -> float:
        return rotary_encoder.steps

    def get_alt() -> float:
        return mpu6050_data()[0]

    az_real = get_az()
    alt_real = get_alt()

    if az > az_real:
        forward_azimuth()
    elif az < az_real:
        backward_azimuth()

    if alt > alt_real:
        forward_altitude()
    elif alt < alt_real:
        backward_altitude()

    if az == az_real:
        stop_azimuth()

    if alt == alt_real:
        stop_altitude()
