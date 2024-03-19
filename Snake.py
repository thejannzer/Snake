
import pygame
import random
from pygame.locals import QUIT, KEYDOWN, K_DOWN, K_UP, K_LEFT, K_RIGHT

# pygame setup
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
tick = 90

# playground
pixel_width = 40
startX = 500
startY = 300
appleX = (200)
appleY = (200)
score = 0

snake_pixel = pygame.Rect(startX, startY, pixel_width, pixel_width)
snake = snake_pixel.copy()

# Variablen für die Richtung der Schlange
snake_direction = "RIGHT"  # Standardrichtung

# apple
apple = pygame.Rect(appleX, appleY, pixel_width, pixel_width)

#newapple
newapple = pygame.Rect(random.randint (200, 1000), random.randint(200, 600), pixel_width, pixel_width )


# Haupt-Schleife
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_DOWN and not snake_direction == "UP":
                snake_direction = "DOWN"
            elif event.key == K_UP and not snake_direction == "DOWN":
                snake_direction = "UP"
            elif event.key == K_LEFT and not snake_direction == "RIGHT":
                snake_direction = "LEFT"
            elif event.key == K_RIGHT and not snake_direction == "LEFT":
                snake_direction = "RIGHT"

    # Bewegung der Schlange basierend auf der Richtung aktualisieren
    if snake_direction == "UP":
        snake_pixel.y -= 2
    elif snake_direction == "DOWN":
        snake_pixel.y += 2
    elif snake_direction == "LEFT":
        snake_pixel.x -= 2
    elif snake_direction == "RIGHT":
        snake_pixel.x += 2

    # Kollision mit dem Rand behandeln
    if snake_pixel.left < 0:
        snake_pixel.right = screen_width
    elif snake_pixel.right > screen_width:
        snake_pixel.left = 0
    elif snake_pixel.top < 0:
        snake_pixel.bottom = screen_height
    elif snake_pixel.bottom > screen_height:
        snake_pixel.top = 0

    #Schlange erweitern
    


    # Kollision mit dem Apfel überprüfen
    if snake_pixel.colliderect(apple):
        appleX = random.randint(0, 1280 - pixel_width)
        appleY = random.randint(0, 720 - pixel_width)
        apple = pygame.Rect(appleX, appleY, pixel_width, pixel_width)
        score = score + 1
        tick = tick + 5


    # Bildschirm aktualisieren
    screen.fill("black")

    pygame.draw.rect(screen, "green", snake_pixel)
    pygame.draw.rect(screen, "red", apple)
    pygame.display.set_caption(f"Score: {score}")



    pygame.display.flip()

    clock.tick(tick)  # Geschwindigkeit der Schlange (je größer, desto schneller)