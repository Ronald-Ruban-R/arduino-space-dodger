
#include <Wire.h>

const byte ADXL345_ADDR = 0x53;

const int buttonPin = 2;

byte readRegister(byte reg) {
  Wire.beginTransmission(ADXL345_ADDR);
  Wire.write(reg);

  if (Wire.endTransmission(false) != 0) {
    return 0xFF;
  }

  Wire.requestFrom(ADXL345_ADDR, (byte)1);

  if (Wire.available()) {
    return Wire.read();
  }

  return 0xFF;
}

bool writeRegister(byte reg, byte value) {
  Wire.beginTransmission(ADXL345_ADDR);
  Wire.write(reg);
  Wire.write(value);
  return Wire.endTransmission() == 0;
}

bool readAcceleration(int16_t &x, int16_t &y, int16_t &z) {
  Wire.beginTransmission(ADXL345_ADDR);
  Wire.write(0x32);  // DATAX0
  if (Wire.endTransmission(false) != 0) {
    return false;
  }

  if (Wire.requestFrom(ADXL345_ADDR, (byte)6) != 6) {
    return false;
  }

  byte x0 = Wire.read();
  byte x1 = Wire.read();
  byte y0 = Wire.read();
  byte y1 = Wire.read();
  byte z0 = Wire.read();
  byte z1 = Wire.read();

  x = (int16_t)((uint16_t)x1 << 8 | x0);
  y = (int16_t)((uint16_t)y1 << 8 | y0);
  z = (int16_t)((uint16_t)z1 << 8 | z0);

  return true;
}

void setup() {
  Serial.begin(115200);
  Wire.begin();

  delay(100);

  byte deviceID = readRegister(0x00);

  pinMode(buttonPin, INPUT_PULLUP);

  Serial.println("ADXL345 test starting...");

  if (deviceID != 0xE5) {
    Serial.print("ERROR: Device ID = 0x");
    Serial.println(deviceID, HEX);
    Serial.println("Expected 0xE5. Check wiring and power.");
    while (true) {
      delay(1000);
    }
  }

  // Full-resolution mode, +/- 2g range
  if (!writeRegister(0x31, 0x08)) {
    Serial.println("ERROR: Could not configure sensor.");
    while (true) {
      delay(1000);
    }
  }

  // Start measurement mode
  if (!writeRegister(0x2D, 0x08)) {
    Serial.println("ERROR: Could not start measurements.");
    while (true) {
      delay(1000);
    }
  }

  Serial.println("ADXL345 detected!");
  Serial.println("X\tY\tZ");
}

void loop() {
  int16_t x, y, z;

  if (readAcceleration(x, y, z)) {
    int buttonState = digitalRead(buttonPin);

    Serial.print(x);
    Serial.print('\t');
    Serial.print(y);
    Serial.print('\t');
    Serial.print(z);
    Serial.print('\t');
    Serial.println(buttonState == LOW ? 1 : 0);
  } else {
    Serial.println("ERROR: Failed to read sensor data");
  }

  delay(100);
}
