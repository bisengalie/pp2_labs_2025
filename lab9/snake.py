import pygame
import random
import time

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Snake variables
snake_pos = [[100, 100], [90, 100], [80, 100]]
snake_direction = "RIGHT"
snake_speed = 10

# Food variables
food_pos = [random.randint(1, WIDTH//10 - 1) * 10, random.randint(1, HEIGHT//10 - 1) * 10]
food_timer = time.time()
food_weight = random.choice([1, 2, 5])  # Different point values

# Score and level
score = 0
level = 1
speed_increment = 2  # Speed increases at each level-up
foods_eaten = 0  # Counter to track how many foods eaten

# Function to generate a new food position
def generate_food():
    global food_timer, food_weight
    while True:
        x = random.randint(1, WIDTH//10 - 1) * 10
        y = random.randint(1, HEIGHT//10 - 1) * 10
        if [x, y] not in snake_pos:  # Ensure food does not spawn on the snake
            food_timer = time.time()  # Reset timer
            food_weight = random.choice([1, 2, 5])  # Random weight
            return [x, y]

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Snake movement logic
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_direction != "DOWN":
        snake_direction = "UP"
    if keys[pygame.K_DOWN] and snake_direction != "UP":
        snake_direction = "DOWN"
    if keys[pygame.K_LEFT] and snake_direction != "RIGHT":
        snake_direction = "LEFT"
    if keys[pygame.K_RIGHT] and snake_direction != "LEFT":
        snake_direction = "RIGHT"

    # Move the snake
    if snake_direction == "UP":
        new_head = [snake_pos[0][0], snake_pos[0][1] - 10]
    elif snake_direction == "DOWN":
        new_head = [snake_pos[0][0], snake_pos[0][1] + 10]
    elif snake_direction == "LEFT":
        new_head = [snake_pos[0][0] - 10, snake_pos[0][1]]
    elif snake_direction == "RIGHT":
        new_head = [snake_pos[0][0] + 10, snake_pos[0][1]]

    # Check for collision with borders
    if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
        print("Game Over! You hit the wall.")
        running = False

    # Check for collision with itself
    if new_head in snake_pos:
        print("Game Over! You hit yourself.")
        running = False

    snake_pos.insert(0, new_head)

    # Check if snake eats food
    if snake_pos[0] == food_pos:
        score += food_weight
        foods_eaten += 1
        food_pos = generate_food()

        # Level up after 3 foods
        if foods_eaten % 3 == 0:
            level += 1
            snake_speed += speed_increment  # Increase speed
    else:
        snake_pos.pop()  # Remove last segment if not eating

    # Food disappears after 5 seconds
    if time.time() - food_timer > 5:
        food_pos = generate_food()

    # Draw the snake
    for pos in snake_pos:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

    # Draw the food
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Display Score and Level
    font = pygame.font.Font(None, 30)
    score_text = font.render(f"Score: {score}  Level: {level}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(snake_speed)

pygame.quit()
