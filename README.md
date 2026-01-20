# Motor Control via Serial (Python)

This project provides a simple Python script to control a robot’s motors by sending commands over a serial connection (UART/USB).

The script is typically used to control motors connected to a microcontroller such as **Arduino** or **ESP32**.

---

## Overview

The Python script:
- Opens a serial connection
- Sends motor speed commands as text
- Controls left and right motors independently

Communication is done using a simple ASCII protocol.

---

## Serial Command Format

Each motor command is sent as a single line:

M <left_speed> <right_speed>


Where:
- `left_speed`  is an integer from `-255` to `255`
- `right_speed` is an integer from `-255` to `255`

### Examples

M 150 150 # Move forward
M 150 -150 # Rotate in place
M 0 0 # Stop

