# Hardware Documentation

## 1. Overview

The hardware controller allows the player to control the Space Dodger game using physical movements and a push button. An Arduino Uno reads the accelerometer and button inputs and sends the data to the Python game through USB serial communication.

## 2. Components Used

| Component | Purpose |
|---|---|
| Arduino Uno | Reads sensor data and sends it to the computer |
| ADXL345 accelerometer | Detects acceleration caused by tilting the controller |
| Push button | Provides a physical shooting input |
| Bidirectional logic-level shifter | Interfaces the sensor's I²C signals with the Arduino's 5V logic |
| Jumper wires | Connect the components |
| USB cable | Powers/programs the Arduino and carries serial data to the computer |

## 3. Component Connections

### ADXL345 Accelerometer

- VCC → Arduino 3.3V
- GND → Common GND
- CS → 3.3V
- SDO → GND
- SDA → Logic-level shifter LV1; corresponding HV1 → Arduino A4
- SCL → Logic-level shifter LV2; corresponding HV2 → Arduino A5

### Logic-Level Shifter

- LV → 3.3V
- HV → 5V
- GND → Common GND

### Push Button

- One terminal → Arduino D2
- Other terminal → GND

The button uses the Arduino's internal pull-up resistor (`INPUT_PULLUP`).

## 4. How the Hardware Works

1. The ADXL345 measures acceleration along its X, Y, and Z axes.
2. The Arduino reads the sensor data over I²C.
3. The push button provides an additional digital input.
4. The Arduino sends the sensor readings and button state to the computer over USB serial.
5. The Python game uses these inputs to control player movement and shooting.

## 5. Communication Settings

- Communication interface: I²C between the Arduino and ADXL345
- Computer interface: USB serial
- Serial baud rate: 115200
- I²C device address: 0x53

## 6. Hardware Notes

- The sensor and Arduino must share a common ground.
- Close the Arduino Serial Monitor before running the Python game if the game needs to access the same serial port.
- The COM port may change depending on the computer and USB connection.

