#!/usr/bin/env python3

import serial
import time


PORT = "/dev/ttyUSB0"   
BAUDRATE = 115200
TIMEOUT = 1


ser = serial.Serial(
    port=PORT,
    baudrate=BAUDRATE,
    timeout=TIMEOUT
)

time.sleep(2)  

print("Serial connection established")


def send_motor_command(left, right):
    """
    Send motor speed command.
    left, right: int [-255, 255]
    """
    command = f"M {left} {right}\n"
    ser.write(command.encode("utf-8"))
    print("Sent:", command.strip())



try:
    # Forward
    send_motor_command(150, 150)
    time.sleep(2)

    # Rotate right
    send_motor_command(150, -150)
    time.sleep(2)

    # Stop
    send_motor_command(0, 0)

except KeyboardInterrupt:
    print("Interrupted")

finally:
    send_motor_command(0, 0)
    ser.close()
    print("Serial connection closed")
