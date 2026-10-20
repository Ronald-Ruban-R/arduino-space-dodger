import pygame
import sys
import random
import serial
import time

pygame.init()


# Arduino tilt-controller setup
ARDUINO_PORT = "COM3"  # Change this if your Arduino uses another port
BAUD_RATE = 115200

arduino = None
tilt_center_x = 0
tilt_speed = 0

button_pressed = False
last_button_shot = 0
button_shot_delay = 200  # milliseconds

try:
    arduino = serial.Serial(ARDUINO_PORT, BAUD_RATE, timeout=0)
    time.sleep(2)  # Allow Arduino to reset after serial connection
    arduino.reset_input_buffer()

    # Calibrate while the sensor is flat and still
    samples = []
    start_time = time.time()

    while time.time() - start_time < 1.0:
        try:
            line = arduino.readline().decode("utf-8").strip()
            values = line.split("\t")

            if len(values) >= 3:
                samples.append(int(values[0]))
        except (ValueError, UnicodeDecodeError):
            pass

    if samples:
        tilt_center_x = sum(samples) / len(samples)

    print("Arduino tilt controller connected.")
    print(f"Calibration center: {tilt_center_x:.1f}")

except serial.SerialException as error:
    print(f"Arduino not connected: {error}")
    print("Keyboard controls will still work.")

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodger")

clock = pygame.time.Clock()

player_x = 370
player_y = 520
player_speed = 5

coloro = 255
colort = 0

chance = 0
give_chance = False

asteroids = []

for i in range(3):
    asteroid = {
        "x": random.randint(0, 740),
        "y": random.randint(-600, 0),
        "speed": random.randint(3,6)
    }
    asteroids.append(asteroid)

score = 0
font = pygame.font.SysFont(None, 36)
 
game_state = "PLAYING"
max_asteroids = 3
stars = []

for i in range(50):
    star = {
        "x": random.randint(0, 800),
        "y": random.randint(0, 600),
        "speed": random.randint(1,3)
    }
    stars.append(star)

bullets = []

explosions = []

explosions.append({
    "x": asteroid["x"],
    "y": asteroid["y"],
    "radius": 5
})

def explosionLoop():
    global explosions

    for e in explosions:
        e["radius"] += 2

        pygame.draw.circle(screen, (255, 165, 0), (e["x"], e["y"]), e["radius"])

        explosions = [ e for e in explosions if e["radius"] < 30]


def readTiltController():
    global tilt_speed, button_pressed

    if arduino is None:
        tilt_speed = 0
        return

    # Read available serial data without blocking the game
    try:
        while arduino.in_waiting:
            line = arduino.readline().decode("utf-8").strip()
            values = line.split("\t")

            if len(values) >= 4:
                button_pressed = values[3] == "1"

            if len(values) >= 3:
                x_value = int(values[0])
                tilt = x_value - tilt_center_x

                # Ignore tiny sensor movements
                deadzone = 20

                if abs(tilt) < deadzone:
                    tilt_speed = 0
                else:
                    # Negative sign matches your successful tilt test
                    tilt_speed = max(
                        -8,
                        min(8, -tilt / 120 * 8)
                    )

    except (ValueError, UnicodeDecodeError, serial.SerialException):
        pass


def keyPress():
    global player_x, player_y, player_speed

    readTiltController()
    player_x += tilt_speed

    keys = pygame.key.get_pressed()

    if (keys[pygame.K_LEFT] or keys[pygame.K_a]):
        player_x -= player_speed

    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
        player_x += player_speed

    if (keys[pygame.K_UP] or keys[pygame.K_w]):
        player_y -= player_speed

    if (keys[pygame.K_DOWN] or keys[pygame.K_s]):
        player_y += player_speed

def eventCont():
    global game_state, score, coloro, colort, player_x, player_y, max_asteroids, asteroids, bullets, chance, give_chance
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if True:
                if event.key == pygame.K_s and game_state == "Game Over!" and chance < 3 and score >= 51:
                    game_state = "PLAYING"
                    score -= 50
                    chance += 1

                    for asteroid in asteroids:
                        asteroid["x"] = random.randint(0, 740)
                        asteroid["y"] = random.randint(-600, 0)
            elif chance>3 and game_state == "PLAYING" and score <= 51:
                continue
            
            if event.key == pygame.K_r and game_state == "Game Over!":
                game_state = "PLAYING"

                score = 0

                coloro = 255
                colort = 0

                player_x = 370
                player_y = 520

                max_asteroids = 3

                chance = 0

                asteroids = []

                for i in range(3):
                    asteroid = {
                        "x": random.randint(0, 740),
                        "y": random.randint(-600, 0),
                        "speed": random.randint(3,6)
                    }
                    asteroids.append(asteroid)

                for asteroid in asteroids:
                    asteroid["x"] = random.randint(0, 740)
                    asteroid["y"] = random.randint(-600, 0)

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE and game_state == "PLAYING":
                bullet = {
                    "x": player_x + 30,
                    "y": player_y
                }

                bullets.append(bullet)


def physicalButtonShoot():
    global last_button_shot, bullets

    now = pygame.time.get_ticks()

    if (
        button_pressed
        and game_state == "PLAYING"
        and now - last_button_shot >= button_shot_delay
    ):
        bullet = {
            "x": player_x + 30,
            "y": player_y
        }

        bullets.append(bullet)
        last_button_shot = now


def playerBoundry():
    global player_x, player_y
    player_x = max(0, min(player_x, 740))
    player_y = max(0, min(player_y, 580))

def bulletCont():
    global bullets
    for bullet in bullets:
        bullet["y"] -= 8

    bullets = [ b for b in bullets if b["y"] > 0]

def highScore():
    global score, max_asteroids, coloro, colort
    if score > 300 and max_asteroids < 5:
        asteroid = {
            "x": random.randint(0, 740),
            "y": random.randint(-600, 0),
            "speed": random.randint(3,6)
        }

        asteroids.append(asteroid)
        max_asteroids += 1

        coloro = 0
        colort = 255

def bulletStar():
    global bullets, game_state, stars
    for bullet in bullets:
        pygame.draw.rect(screen, (255, 255, 0), (bullet["x"], bullet["y"], 5, 10))

    for star in stars:
        if game_state == "PLAYING":
            star["y"] += star["speed"]

        if star["y"] > 600:
            star["y"] = 0
            star["x"] = random.randint(0, 800)

        pygame.draw.circle(screen, (255, 255, 255), (star["x"], star["y"]), 2)

def asteroidLoop():
    global asteroids, score,game_state, coloro, colort, bullets, player_x, player_y
    for asteroid in asteroids:
        if game_state == "PLAYING":
            asteroid["y"] += asteroid["speed"] + score*0.02

        if asteroid["y"] > 600:
            asteroid["y"] = random.randint(-200, -50)
            asteroid["x"] = random.randint(0, 740) 

        pygame.draw.circle(screen, (coloro, 0, colort), (asteroid["x"], asteroid["y"]), 20)
    
        for bullet in bullets:
            if (bullet["x"] > asteroid["x"] - 20 and bullet["x"] < asteroid["x"] + 20 and bullet["y"] > asteroid["y"] - 20 and bullet["y"] < asteroid["y"] + 20):
                x = asteroid["x"]
                y = asteroid["y"]

                explosions.append({
                "x": asteroid["x"],
                "y": asteroid["y"],
                "radius": 5
                })

                asteroid["y"] = random.randint(0, 200)
                asteroid["x"] = random.randint(0, 740)

                bullets.remove(bullet)

                score += 10

                

        if (player_x < asteroid["x"] + 20 and player_x + 60 > asteroid["x"] - 20 and player_y < asteroid["y"] + 20 and player_y + 20 > asteroid["y"] - 20):
            game_state = "Game Over!"

def drawPlayer():
    global player_x, player_y
    pygame.draw.polygon(screen, (0, 255, 0), [(player_x, player_y+20), (player_x + 60, player_y + 20), (player_x + 30, player_y - 20) ])
    pygame.draw.rect(screen, (0, 255, 0), (player_x , player_y + 20, 60, 30))

def gameOver():
    global game_state, score, i
    if game_state == "Game Over!":
        if chance<3 and score >= 51:
            resume_text = font.render(f"Resume press S (50 points will be taken), chance {3-chance}", True, (255, 255, 255))
            screen.blit(resume_text, (100, 250))

        text = font.render("Game Over - Press R", True, (255, 255, 255))
        screen.blit(text, (250, 300))

        score_text = font.render("Score" + str(int(score)), True, (255, 255, 255))
        screen.blit(score_text, (250, 340))

def scorePrint():
    global score
    score_text = font.render("Score" + str(int(score)), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))


while True:

    eventCont()
    if game_state == "PLAYING":
        keyPress()
        physicalButtonShoot()

    playerBoundry() 
    bulletCont()
    highScore()

    screen.fill((0, 0, 0))

    bulletStar()
    asteroidLoop()

    if game_state == "PLAYING":
        score += 0.1
    
    drawPlayer()

    explosionLoop()

    gameOver() 
    scorePrint()
    
    pygame.display.update()
    clock.tick(60)


