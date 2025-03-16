import pygame

pygame.init()

# Screen settings
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Red Ball Movement")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Ball settings
radius = 25
x, y = WIDTH // 2, HEIGHT // 2  # Start position at center
speed = 20  # Movement speed

running = True
while running:
    pygame.time.delay(50)  # Small delay for smooth movement
    screen.fill(WHITE)  # Clear screen

    # Draw the red ball
    pygame.draw.circle(screen, RED, (x, y), radius)

    pygame.display.flip()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Move ball but prevent it from going out of bounds
            if event.key == pygame.K_UP and y - radius - speed >= 0:
                y -= speed
            elif event.key == pygame.K_DOWN and y + radius + speed <= HEIGHT:
                y += speed
            elif event.key == pygame.K_LEFT and x - radius - speed >= 0:
                x -= speed
            elif event.key == pygame.K_RIGHT and x + radius + speed <= WIDTH:
                x += speed

pygame.quit()