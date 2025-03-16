import pygame

pygame.init()
pygame.mixer.init()

# List of music files (replace with actual paths)
music_files = ["song1.mp3", "song2.mp3", "song3.mp3"]
current_track = 0

# Function to play music
def play_music(track):
    """Loads and plays a track from the music list."""
    pygame.mixer.music.load(music_files[track])
    pygame.mixer.music.play()

# Start the first track
play_music(current_track)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Play/Pause
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_s:  # Stop
                pygame.mixer.music.stop()
            elif event.key == pygame.K_RIGHT:  # Next track
                current_track = (current_track + 1) % len(music_files)
                play_music(current_track)
            elif event.key == pygame.K_LEFT:  # Previous track
                current_track = (current_track - 1) % len(music_files)
                play_music(current_track)

pygame.quit()