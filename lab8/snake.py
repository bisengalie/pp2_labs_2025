import pygame
import random

# Initialize Pygame
pygame.init()

# Window settings
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 20  # Size of each snake segment
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game with Levels")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Snake settings
snake = [(100, 100), (80, 100), (60, 100)]
direction = (GRID_SIZE, 0)  # Moving right
speed = 10  # Initial speed
score = 0
level = 1

# Function to generate food at a valid position
def generate_food():
    while True:
        food_x = random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        food_y = random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        if (food_x, food_y) not in snake:  # Ensure food is not on the snake
            return food_x, food_y

food = generate_food()

# Font for score display
font = pygame.font.Font(None, 30)

# Main game loop
running = True
while running:
    pygame.time.delay(100 - speed * 2)  # Adjust speed
    screen.fill(BLACK)  # Clear screen

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Snake movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and direction != (GRID_SIZE, 0):
        direction = (-GRID_SIZE, 0)
    if keys[pygame.K_RIGHT] and direction != (-GRID_SIZE, 0):
        direction = (GRID_SIZE, 0)
    if keys[pygame.K_UP] and direction != (0, GRID_SIZE):
        direction = (0, -GRID_SIZE)
    if keys[pygame.K_DOWN] and direction != (0, -GRID_SIZE):
        direction = (0, GRID_SIZE)

    # Update snake position
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    # Check for collisions (walls or self)
    if new_head in snake or not (0 <= new_head[0] < WIDTH and 0 <= new_head[1] < HEIGHT):
        running = False

    snake.insert(0, new_head)  # Add new head

    # Check if the snake eats the food
    if new_head == food:
        score += 1
        food = generate_food()
        if score % 3 == 0:  # Increase level every 3 food items
            level += 1
            speed += 2  # Increase speed
    else:
        snake.pop()  # Remove tail if no food is eaten

    # Draw food
    pygame.draw.rect(screen, RED, (*food, GRID_SIZE, GRID_SIZE))

    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, GRID_SIZE, GRID_SIZE))

    # Display score and level
    score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()