# Software Documentation

## 1. Overview

Space Dodger is a Python game built using Pygame and controlled using an Arduino-based physical controller. The Arduino reads the accelerometer and button, then transmits the input data through serial communication. Python receives this data and translates it into game actions.

## 2. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Implements the game logic and hardware communication |
| Pygame | Handles graphics, keyboard input, collision detection, and the game loop |
| PySerial | Reads data from the Arduino's serial port |
| Arduino C++ | Reads sensor data and transmits controller inputs |
| Wire library | Provides I²C communication with the ADXL345 |

## 3. Software Architecture

### Arduino Program

The Arduino sketch:
- Initializes serial communication at 115200 baud.
- Initializes I²C communication.
- Checks the ADXL345 device ID.
- Configures the accelerometer and enables measurements.
- Reads X, Y, and Z acceleration values.
- Reads the push-button state.
- Transmits the values as tab-separated serial data.

### Python Game

The Python game:
- Initializes the Pygame window and game objects.
- Opens the Arduino serial port using PySerial.
- Reads the incoming controller data.
- Calibrates the accelerometer's X-axis center.
- Applies a dead zone to reduce unwanted movement.
- Converts tilt into horizontal player movement.
- Uses the physical button to shoot bullets.
- Supports keyboard movement and Spacebar shooting.
- Updates asteroids, bullets, collisions, score, and game state.
- Renders the game at a target frame rate of 60 FPS.

## 4. Controller Data Format

The Arduino sends four values separated by tab characters:

X    Y    Z    BUTTON

- X: X-axis accelerometer reading
- Y: Y-axis accelerometer reading
- Z: Z-axis accelerometer reading
- BUTTON: `1` when pressed, `0` when released

Each data line ends with a newline so the Python program can process individual readings.

## 5. Input Processing

### Tilt-Based Movement

The Python program compares the current X-axis reading with the calibrated center value. It applies a dead zone to ignore small fluctuations and converts the remaining tilt into horizontal movement.

### Button-Based Shooting

When the received button state indicates a press, the game creates a bullet. A cooldown prevents continuous bullet creation while the button remains pressed.

### Keyboard Controls

The game also supports keyboard input so it can be played or tested without relying entirely on the physical controller.

## 6. Dependencies

Python packages are listed in `requirements.txt`:

- `pygame`
- `pyserial`

The Arduino sketch uses the `Wire` library for I²C communication.

## 7. Running the Software

1. Upload the Arduino sketch to the Arduino Uno.
2. Connect the Arduino to the computer.
3. Close the Arduino Serial Monitor.
4. Install the Python dependencies.
5. Confirm the correct serial port is configured in the game.
6. Run `game.py`.

## 8. Current Limitations

- The configured serial port may need to be changed on another computer.
- Tilt sensitivity and calibration may require adjustment for different users or sensor orientations.
- The game requires the Arduino controller to be connected for physical input; keyboard controls provide an alternative.

