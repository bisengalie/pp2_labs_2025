import pygame
import random

# Initialize Pygame
pygame.init()

# Window settings
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Game with Coins")

# Load images
car_image = pygame.image.load("car.png")  # Car image
coin_image = pygame.image.load("coin.png")  # Coin image

# Resize images
car_width, car_height = 50, 80
car_image = pygame.transform.scale(car_image, (car_width, car_height))
coin_size = 30
coin_image = pygame.transform.scale(coin_image, (coin_size, coin_size))

# Colors
WHITE = (255, 255, 255)
ROAD_COLOR = (50, 50, 50)

# Initial car position
car_x = WIDTH // 2 - car_width // 2
car_y = HEIGHT - car_height - 20
car_speed = 5

# Coin properties
coin_x = random.randint(50, WIDTH - 50)
coin_y = random.randint(-200, -50)
coin_speed = 4
coin_collected = 0  # Coin counter

# Font for score display
font = pygame.font.Font(None, 36)

# Main game loop
running = True
while running:
    screen.fill(ROAD_COLOR)  # Fill background with road color

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Car movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 50:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - car_width - 50:
        car_x += car_speed

    # Move coin down
    coin_y += coin_speed

    # Check if the car collects the coin
    if (car_x < coin_x < car_x + car_width or car_x < coin_x + coin_size < car_x + car_width) and \
       (car_y < coin_y < car_y + car_height):
        coin_collected += 1  # Increase score
        coin_x = random.randint(50, WIDTH - 50)  # New coin position
        coin_y = random.randint(-200, -50)

    # Reset coin if it goes off-screen
    if coin_y > HEIGHT:
        coin_x = random.randint(50, WIDTH - 50)
        coin_y = random.randint(-200, -50)

    # Draw elements
    screen.blit(car_image, (car_x, car_y))
    screen.blit(coin_image, (coin_x, coin_y))

    # Display score
    score_text = font.render(f"Coins: {coin_collected}", True, WHITE)
    screen.blit(score_text, (WIDTH - 120, 10))

    pygame.display.update()
    pygame.time.delay(30)  # Small delay for smooth movement

pygame.quit()