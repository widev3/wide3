# https://38-3d.co.uk/it/blogs/blog-38-3d-2/usando-mpu-6050-con-il-raspberry-pi
# https://www.instructables.com/How-to-Use-the-MPU6050-With-the-Raspberry-Pi-4/

import time
import math
import smbus2

MPU6050_ADDR = 0x68
PWR_MGMT_1 = 0x6B
ACCEL_XOUT_H = 0x3B
GYRO_XOUT_H = 0x43


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


def main():
    bus = None
    while True:
        if not bus:
            bus = start_restart()
        try:
            # gyro_x = read_raw_data(bus, GYRO_XOUT_H)
            # gyro_y = read_raw_data(bus, GYRO_XOUT_H + 2)
            # gyro_z = read_raw_data(bus, GYRO_XOUT_H + 4)
            # gyro_x /= 131.0
            # gyro_y /= 131.0
            # gyro_z /= 131.0
            # print(f"Gyroscope: X={gyro_x:.2f}, Y={gyro_y:.2f}, Z={gyro_z:.2f}")

            accel_x = read_raw_data(bus, ACCEL_XOUT_H)
            accel_y = read_raw_data(bus, ACCEL_XOUT_H + 2)
            accel_z = read_raw_data(bus, ACCEL_XOUT_H + 4)
            accel_x /= 16384.0 / 9.81
            accel_y /= 16384.0 / 9.81
            accel_z /= 16384.0 / 9.81

            a = math.sqrt(accel_x**2 + accel_y**2 + accel_z**2)
            if a == 0:
                continue

            thetaX = math.degrees(math.acos(accel_x / a))
            thetaY = math.degrees(math.acos(accel_y / a))
            thetaZ = math.degrees(math.acos(accel_z / a))
            print(f"Accelerometer: X={accel_x:.2f}, Y={accel_y:.2f}, Z={accel_z:.2f}")
            print(f"Angle: X={thetaX:.2f}, Y={thetaY:.2f}, Z={thetaZ:.2f}")

            time.sleep(1)
        except:
            bus = start_restart()


main()
