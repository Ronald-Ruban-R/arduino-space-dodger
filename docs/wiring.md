# Wiring Guide — Arduino Space Dodger

## 1. Overview

This guide explains how to connect the ADXL345 accelerometer and push button to an Arduino Uno for the Space Dodger game controller.

The ADXL345 communicates with the Arduino using I²C. A bidirectional logic-level shifter is used for the I²C signal connections in this setup.

## 2. Components Required

- Arduino Uno
- ADXL345 accelerometer module (MOD-QC0157)
- Bidirectional logic-level shifter
- Push button
- Jumper wires
- USB cable

## 3. ADXL345 to Logic-Level Shifter

| ADXL345 pin | Connection   |
| ----------- | ------------ |
| VCC         | Arduino 3.3V |
| GND         | Common GND   |
| CS          | Arduino 3.3V |
| SDO         | GND          |
| SDA         | Shifter LV1  |
| SCL         | Shifter LV2  |

## 4. Logic-Level Shifter Connections

| Shifter pin | Connection       |
| ----------- | ---------------- |
| LV          | Arduino 3.3V     |
| HV          | Arduino 5V       |
| GND         | Common GND       |
| LV1         | ADXL345 SDA      |
| HV1         | Arduino A4 (SDA) |
| LV2         | ADXL345 SCL      |
| HV2         | Arduino A5 (SCL) |

**Important:** Connect the corresponding LV and HV channels to the same signal. LV1 connects to HV1, and LV2 connects to HV2.

## 5. Push Button Connections

| Push button terminal | Connection             |
| -------------------- | ---------------------- |
| Terminal 1           | Arduino digital pin D2 |
| Terminal 2           | Arduino GND            |

The Arduino sketch uses `pinMode(buttonPin, INPUT_PULLUP)`. Therefore:

- Button released → `HIGH`
- Button pressed → `LOW`

The sketch converts this into serial output where `1` means pressed and `0` means released.

## 6. Arduino-to-Computer Connection

Connect the Arduino Uno to the computer using a USB cable.

The USB connection provides:

- Power to the Arduino.
- A way to upload the Arduino sketch.
- Serial communication between the Arduino and Python game.

The Arduino sketch communicates at **115200 baud**.

## 7. I²C Configuration

The Arduino sketch uses the following configuration:

- SDA: A4
- SCL: A5
- ADXL345 I²C address: `0x53`
- CS: HIGH, selecting I²C mode
- SDO: LOW, selecting address `0x53`

## 8. Wiring Checklist

- [ ] ADXL345 VCC connected to 3.3V.
- [ ] All grounds connected together.
- [ ] CS connected to 3.3V.
- [ ] SDO connected to GND.
- [ ] SDA and SCL connected through the corresponding level-shifter channels.
- [ ] Level shifter LV connected to 3.3V and HV connected to 5V.
- [ ] Push button connected between D2 and GND.
- [ ] Arduino connected to the computer through USB.

## 9. Troubleshooting

### ADXL345 not detected

- Check the VCC and GND connections.
- Check SDA and SCL connections.
- Confirm that the Arduino sketch expects device ID `0xE5`.
- Check the I²C address configuration.

### Python cannot connect to Arduino

- Check the COM port configured in the Python code.
- Close the Arduino Serial Monitor before running the game.
- Confirm that the baud rate is 115200.

### Button does not work

- Check the D2 and GND connections.
- Verify that the sketch uses `INPUT_PULLUP`.
- Confirm that the serial output changes to `1` when the button is pressed.

## 10. Reference Images

Add a clear photo of the actual circuit to `../images/circuit.jpg` when available.


