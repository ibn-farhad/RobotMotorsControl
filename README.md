# Motor Control via Serial (Python)

This project provides a simple Python script to control a robot’s motors
by sending commands over a serial connection (UART / USB).

It is intended for quick testing and manual control of motors connected
to a microcontroller such as **Arduino** or **ESP32**.

---

## Features

- Serial communication using `pyserial`
- Independent left and right motor control
- Human-readable command protocol
- **Keyboard-based manual control**
- Safe shutdown (motors stop on exit)

---

## Serial Command Protocol

Commands are sent as text lines:

M <left_speed> <right_speed>


Where:
- `left_speed`  ∈ `[-255, 255]`
- `right_speed` ∈ `[-255, 255]`

### Examples

M 150 150 # Move forward
M -150 -150 # Move backward
M -150 150 # Rotate left
M 150 -150 # Rotate right
M 0 0 # Stop

---

## Keyboard Controls

When the script is running, use the following keys:

| Key | Action |
|---|---|
| `w` | Move forward |
| `s` | Move backward |
| `a` | Rotate left |
| `d` | Rotate right |
| `x` | Stop motors |
| `q` | Quit (stop motors and exit) |

---

## Requirements

- Python 3
- `pyserial`

Install dependency:

```bash
pip install pyserial
```

---
## Report


Created repo on Git
```bash
git pull

touch README.md
touch motors_control.py
touch git .gitignore
code .
```

Made changes on the files
Added required lines to the gitignore

```bash
git status

git add --all

git commit -m ""

git push -u origin main
```

Generated token to push. Wrote it while asked

```bash
git checkout -b keyboard_control

```

Made changes on the files

```bash
git add --all
git commint -m ""

git push --set-upstream origin keyboard_control
```
Made a pull - request, confirmed it.

Then 
```bash
git checkout main

git pull
```
Made this changes!!!

## Impressions
Seeing the possibilities and conveniences of this technology, I regret not using it to this day! In my future projects, I will always use Git.