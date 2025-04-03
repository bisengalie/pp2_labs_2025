import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Load assets
player_car = pygame.image.load("C:\Users\erasy\Desktop\labs\lab9\player_car.png")  # Replace with your image
enemy_car = pygame.image.load("C:\Users\erasy\Desktop\labs\lab9\enemy_car.png")  # Replace with your image
coin_img = pygame.image.load("C:\Users\erasy\Desktop\labs\lab9\coin.png")  # Replace with your image

# Resize images
player_car = pygame.transform.scale(player_car, (50, 100))
enemy_car = pygame.transform.scale(enemy_car, (50, 100))
coin_img = pygame.transform.scale(coin_img, (30, 30))

# Game variables
player_x = WIDTH // 2 - 25
player_y = HEIGHT - 120
player_speed = 5

enemy_x = random.randint(100, WIDTH - 100)
enemy_y = -100
enemy_speed = 5

coins = []
score = 0
coins_needed_for_speedup = 5  # Speed increases every 5 coins

# Generate a new coin
def create_coin():
    x = random.randint(100, WIDTH - 100)
    y = random.randint(100, HEIGHT - 100)
    value = random.choice([1, 2, 5])  # Random coin values
    return {"x": x, "y": y, "value": value}

# Create initial coins
for _ in range(3):
    coins.append(create_coin())

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 100:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - 150:
        player_x += player_speed

    # Enemy movement
    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = -100
        enemy_x = random.randint(100, WIDTH - 100)

    # Coin collection
    for coin in coins[:]:
        if player_x < coin["x"] < player_x + 50 and player_y < coin["y"] < player_y + 100:
            score += coin["value"]
            coins.remove(coin)
            coins.append(create_coin())

    # Speed increase after collecting enough coins
    if score >= coins_needed_for_speedup:
        enemy_speed += 1
        coins_needed_for_speedup += 5  # Next increase threshold

    # Drawing elements
    screen.blit(player_car, (player_x, player_y))
    screen.blit(enemy_car, (enemy_x, enemy_y))

    for coin in coins:
        screen.blit(coin_img, (coin["x"], coin["y"]))

    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Coins: {score}", True, BLACK)
    screen.blit(score_text, (WIDTH - 150, 10))

    pygame.display.update()
    clock.tick(30)

pygame.quit()
