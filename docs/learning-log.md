# Learning Log — Arduino Space Dodger

This log documents the development of Space Dodger, from the initial game design to hardware-based player controls.

## Development Journey

### 1. Created the Initial Shooter

Started by creating the basic game with a square-shaped player. This helped establish the initial game structure and player movement.

**Learning:** Building the basic game loop and handling player movement in Pygame.

### 2. Improved the Player Design

Changed the original square-shaped player into a more recognizable spaceship shape.

**Learning:** Improving game visuals and representing game objects using shapes.

### 3. Added the Shooting Mechanism

Implemented a shooting mechanism that allows the player to fire bullets at incoming asteroids.

**Learning:** Managing bullet objects, movement, and interactions between game objects.

### 4. Introduced Difficulty Progression

Added a difficulty change after reaching 300 points, increasing the number of asteroids to make the game more challenging.

**Learning:** Connecting game difficulty to the player's score and adjusting gameplay dynamically.

### 5. Fixed Asteroid Spawning After Restart

Discovered that the increased number of asteroids remained unchanged even after restarting the game. Fixed the issue so the asteroid count resets correctly when a new game begins.

**Learning:** Managing game state, resetting variables, and debugging behavior that persists across game sessions.

### 6. Added Explosion Effects

Implemented explosions when the player collides with an asteroid.

Initially, the explosions appeared somewhere other than the actual collision location. Debugged and corrected the positioning so the effect appears at the appropriate location.

**Learning:** Tracking object coordinates, handling collision events, and debugging visual effects.

### 7. Integrated Tilt-Based Movement

Connected an ADXL345 accelerometer to an Arduino Uno and integrated the controller with the Python game through serial communication.

The player can now move horizontally by tilting the physical controller.

**Learning:** Reading sensor data, using serial communication between Arduino and Python, calibrating sensor input, and translating physical movement into game controls.

### 8. Added Physical Button Shooting

Connected a push button to the Arduino and integrated it into the game so the player can shoot using the physical button instead of relying only on the keyboard.

**Learning:** Reading digital inputs, transmitting button states over serial communication, and integrating multiple physical controls into an existing game.

## Current Result

Space Dodger combines a Pygame-based space shooter with an Arduino-powered physical controller.

Current features include:

- Spaceship movement using accelerometer tilt.
- Shooting using a physical push button.
- Keyboard movement and Spacebar shooting.
- Asteroid spawning and collision detection.
- Score-based difficulty progression.
- Bullet mechanics and explosion effects.
- Game restart and resume functionality.

## Key Takeaways

- Building a project incrementally makes complex features easier to manage.
- Debugging unexpected behavior is an important part of development.
- Game state must be handled carefully when restarting a game.
- Physical sensors and software can communicate through serial data.
- Hardware inputs
