import pygame
import time
import os

pygame.init()
pygame.mixer.init()

# Screen settings
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock, Music Player & Moving Ball")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Load images for Mickey Clock
mickey = pygame.image.load("mickey.png")  # Main Mickey image
minute_hand = pygame.image.load("right_hand.png")  # Minute hand
second_hand = pygame.image.load("left_hand.png")  # Second hand

# Set clock center
center = (WIDTH // 2, HEIGHT // 2)

# Music player setup
music_files = ["song1.mp3", "song2.mp3", "song3.mp3"]  # Replace with real file paths
current_track = 0

def play_music(track):
    """Load and play a music track"""
    pygame.mixer.music.load(music_files[track])
    pygame.mixer.music.play()

play_music(current_track)  # Start the first track

# Ball setup
radius = 25
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_speed = 20

# Main loop
running = True
while running:
    screen.fill(WHITE)

    # ----- MICKEY CLOCK -----
    screen.blit(mickey, (0, 0))  # Draw Mickey

    # Get the current time
    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min

    # Calculate angles for rotation
    minute_angle = -6 * minutes
    second_angle = -6 * seconds

    # Rotate hands
    rotated_minute_hand = pygame.transform.rotate(minute_hand, minute_angle)
    rotated_second_hand = pygame.transform.rotate(second_hand, second_angle)

    # Get new hand positions
    rect_m = rotated_minute_hand.get_rect(center=center)
    rect_s = rotated_second_hand.get_rect(center=center)

    screen.blit(rotated_minute_hand, rect_m)
    screen.blit(rotated_second_hand, rect_s)

    # ----- MOVING BALL -----
    pygame.draw.circle(screen, RED, (ball_x, ball_y), radius)

    pygame.display.flip()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # --- MUSIC PLAYER CONTROLS ---
            if event.key == pygame.K_SPACE:  # Play/Pause
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_s:  # Stop music
                pygame.mixer.music.stop()
            elif event.key == pygame.K_RIGHT:  # Next track
                current_track = (current_track + 1) % len(music_files)
                play_music(current_track)
            elif event.key == pygame.K_LEFT:  # Previous track
                current_track = (current_track - 1) % len(music_files)
                play_music(current_track)

            # --- BALL MOVEMENT ---
            elif event.key == pygame.K_UP and ball_y - radius - ball_speed >= 0:
                ball_y -= ball_speed
            elif event.key == pygame.K_DOWN and ball_y + radius + ball_speed <= HEIGHT:
                ball_y += ball_speed
            elif event.key == pygame.K_LEFT and ball_x - radius - ball_speed >= 0:
                ball_x -= ball_speed
            elif event.key == pygame.K_RIGHT and ball_x + radius + ball_speed <= WIDTH:
                ball_x += ball_speed

pygame.quit()
