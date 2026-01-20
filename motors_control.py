import serial
import time


# CONFIGURATION

PORT = "/dev/ttyUSB0"   # Linux
BAUDRATE = 115200
TIMEOUT = 1
SPEED = 150             # Default motor speed



# SERIAL CONNECTION


ser = serial.Serial(PORT, BAUDRATE, timeout=TIMEOUT)
time.sleep(2)

print("Serial connection established")


# MOTOR COMMAND FUNCTION

def send_motor_command(left, right):
    command = f"M {left} {right}\n"
    ser.write(command.encode("utf-8"))
    print("Sent:", command.strip())


# KEYBOARD CONTROL LOOP

print("""
Control keys:
  w - forward
  s - backward
  a - left
  d - right
  x - stop
  q - quit
""")

try:
    while True:
        key = input("Command: ").strip().lower()

        if key == "w":
            send_motor_command(SPEED, SPEED)
        elif key == "s":
            send_motor_command(-SPEED, -SPEED)
        elif key == "a":
            send_motor_command(-SPEED, SPEED)
        elif key == "d":
            send_motor_command(SPEED, -SPEED)
        elif key == "x":
            send_motor_command(0, 0)
        elif key == "q":
            break
        else:
            print("Unknown command")

except KeyboardInterrupt:
    pass

finally:
    send_motor_command(0, 0)
    ser.close()
    print("Motors stopped. Serial closed.")
