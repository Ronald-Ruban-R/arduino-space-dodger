# arduino-space-dodger
A Python Pygame space shooter controlled using an Arduino Uno, ADXL345 accelerometer, and physical button.

#  Arduino Space Dodger

**A space shooter game controlled using real-world motion and a physical button.**

Arduino Space Dodger combines Python game development with embedded hardware. An Arduino Uno reads motion data from an ADXL345 accelerometer and a physical button, then sends the readings to a Python application over serial communication. The game uses this input to control the spaceship.

##  Project Overview

The project explores how embedded hardware can interact with desktop software in real time.

Instead of relying only on a keyboard, the player can tilt the accelerometer to move the spaceship and press a physical button to shoot bullets.

### Features

- **Motion-based movement:** Tilt the ADXL345 accelerometer to control the spaceship.
- **Physical button control:** Shoot bullets using a hardware button connected to the Arduino.
- **Keyboard controls:** Retain keyboard movement and shooting as alternative controls.
- **Real-time communication:** Transfer sensor and button readings from Arduino to Python using serial communication.
- **Game mechanics:** Dodge asteroids, shoot bullets, track scores, and handle collisions.
- **Calibration:** Establish a reference position for the accelerometer when the game starts.

## 🛠️ Hardware Requirements

| Component | Purpose |
|---|---|
| Arduino Uno | Reads sensor and button inputs |
| ADXL345 accelerometer | Detects changes in orientation |
| Push button | Physical shooting control |
| Bidirectional logic-level shifter | Adapts I²C signal levels between the sensor and Arduino |
| Jumper wires | Electrical connections |
| USB cable | Power, programming, and serial communication |

##  Software and Technologies

- Python
- Pygame — game graphics and game loop
- PySerial — serial communication between Python and Arduino
- Arduino C++ — sensor interfacing and hardware input handling
- Arduino Wire library — I²C communication with the ADXL345

## 🔌 Hardware Connections

### ADXL345 to Arduino Uno

The ADXL345 communicates with the Arduino over I²C through a bidirectional logic-level shifter.

| ADXL345 / Level Shifter | Connection |
|---|---|
| ADXL345 VCC | Arduino 3.3V |
| ADXL345 GND | Common GND |
| ADXL345 CS | 3.3V |
| ADXL345 SDO | GND |
| Shifter LV | 3.3V |
| Shifter HV | 5V |
| Shifter GND | Common GND |
| Shifter LV1 | ADXL345 SDA |
| Shifter HV1 | Arduino A4 (SDA) |
| Shifter LV2 | ADXL345 SCL |
| Shifter HV2 | Arduino A5 (SCL) |

### Push Button

| Button terminal | Connection |
|---|---|
| One terminal | Arduino digital pin D2 |
| Other terminal | GND |

The sketch uses `INPUT_PULLUP`, so the input reads LOW when the button is pressed.

**Wiring note:** Verify the pin labels and voltage requirements of your particular ADXL345 breakout board and logic-level shifter before powering the circuit.

##  Project Structure

```text
arduino-space-dodger/
├── README.md
├── requirements.txt
├── .gitignore
├── game/
│   └── game.py
├── arduino/
│   └── space_dodger_controller/
│       └── space_dodger_controller.ino
├── docs/
│   ├── hardware.md
│   ├── software.md
│   ├── wiring.md
│   └── learning-log.md
├── images/
│   ├── circuit.jpg
│   └── gameplay.png
└── tests/
    └── README.md
```

*This is the planned repository structure. Add the files and images as they are created.*

## ⚙️ Setup and Installation

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd arduino-space-dodger
```

Replace `YOUR_REPOSITORY_URL` with your GitHub repository URL.

### 2. Create and activate a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, consult the Python documentation or use the appropriate activation method for your terminal.

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Upload the Arduino sketch

1. Open `arduino/space_dodger_controller/space_dodger_controller.ino` in the Arduino IDE.
2. Select the appropriate Arduino Uno board and COM port.
3. Upload the sketch.
4. Close the Arduino Serial Monitor before running the Python game.

### 5. Configure the serial port

The Python game currently uses `COM3` at `115200` baud. Update the port in the Python code if your Arduino appears under a different COM port.

### 6. Run the game

```powershell
python game/game.py
```

##  Controls

| Input | Action |
|---|---|
| Tilt the accelerometer | Move the spaceship horizontally |
| Physical button | Shoot bullets |
| Arrow keys / WASD | Keyboard movement |
| Spacebar | Shoot bullets |
| R | Restart after game over |
| S | Resume after game over, if enough score is available |

The game may use additional keyboard inputs depending on the current implementation.

##  How It Works

```text
ADXL345 Accelerometer + Push Button
                 |
                 v
           Arduino Uno
        (Arduino C++ / I²C)
                 |
                 v
          Serial over USB
          (115200 baud)
                 |
                 v
       Python + PySerial
       (Read input data)
                 |
                 v
          Pygame Game
      (Movement and shooting)
```

1. The ADXL345 measures acceleration along its X, Y, and Z axes.
2. The Arduino reads the accelerometer registers through I²C and checks the button state.
3. The Arduino transmits the readings over USB serial.
4. Python reads and parses the incoming data using PySerial.
5. The game converts the sensor readings into spaceship movement and the button state into shooting input.

##  What I'm Learning

This project is a practical way to explore the connection between embedded systems and software development.

Key learning areas include:

- I²C communication and sensor register configuration.
- Reading and combining multi-byte sensor data.
- Digital inputs and active-low button logic.
- Serial communication between a microcontroller and a computer.
- Python input processing and Pygame game loops.
- Integrating physical controls with an existing software application.
- Debugging hardware and software together.

##  Future Improvements

- Add a dedicated serial-port configuration option.
- Improve sensor calibration and movement sensitivity.
- Handle serial disconnections and invalid sensor data more robustly.
- Separate the game logic, hardware communication, and configuration into modules.
- Add unit tests for input parsing and game logic.
- Record a short demonstration video and add real hardware and gameplay photographs.
- Document known limitations and troubleshooting steps.

##  Demonstration

Screenshots, circuit photographs, and a gameplay video will be added here as the project documentation develops.

##  License

No license has been selected yet. A license can be added when the repository is ready for public sharing.
