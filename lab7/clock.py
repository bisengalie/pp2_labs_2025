import pygame
import time

pygame.init()

# Screen settings
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

# Load images
mickey = pygame.image.load("mickey.png")  # Main Mickey image
minute_hand = pygame.image.load("right_hand.png")  # Minute hand
second_hand = pygame.image.load("left_hand.png")  # Second hand

# Center of the screen (pivot point for rotation)
center = (WIDTH // 2, HEIGHT // 2)

running = True
while running:
    screen.fill((255, 255, 255))  # White background
    screen.blit(mickey, (0, 0))  # Draw Mickey image

    # Get the current system time
    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min

    # Calculate rotation angles
    minute_angle = -6 * minutes  # 360° / 60 minutes = 6° per minute
    second_angle = -6 * seconds  # 360° / 60 seconds = 6° per second

    # Rotate hands
    rotated_minute_hand = pygame.transform.rotate(minute_hand, minute_angle)
    rotated_second_hand = pygame.transform.rotate(second_hand, second_angle)

    # Get new positions and draw hands
    rect_m = rotated_minute_hand.get_rect(center=center)
    rect_s = rotated_second_hand.get_rect(center=center)

    screen.blit(rotated_minute_hand, rect_m)
    screen.blit(rotated_second_hand, rect_s)

    pygame.display.flip()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()