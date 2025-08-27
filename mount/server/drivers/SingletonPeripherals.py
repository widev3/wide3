import drivers.is_raspberry


class SingletonPeripherals:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(SingletonPeripherals, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, "_initialized") and self._initialized:
            return

        self._initialized = True

        if drivers.is_raspberry.it_is():
            import RPi.GPIO as GPIO
            from gpiozero import PWMLED
            from gpiozero import RotaryEncoder
            from gpiozero import TonalBuzzer

            self.MPU6050_ADDR = 0x68
            self.PWR_MGMT_1 = 0x6B
            self.ACCEL_XOUT_H = 0x3B
            self.GYRO_XOUT_H = 0x43
            self.mpu6050_bus = None

            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)

            # azimuth motor
            self.ENA = 18
            self.IN1 = 23
            self.IN2 = 24
            self.pwm_a = PWMLED(self.ENA)
            GPIO.setup(self.IN1, GPIO.OUT)
            GPIO.setup(self.IN2, GPIO.OUT)

            # altitude motor
            self.ENB = 12
            self.IN3 = 8
            self.IN4 = 25
            self.pwm_b = PWMLED(self.ENB)
            GPIO.setup(self.IN3, GPIO.OUT)
            GPIO.setup(self.IN4, GPIO.OUT)

            # encoder
            self.PINA = 14
            self.PINB = 15
            self.rotary_encoder = RotaryEncoder(
                a=self.PINA,
                b=self.PINB,
                wrap=True,
                max_steps=360,
            )

            TBPIN = 4
            self.tb = TonalBuzzer(TBPIN)
