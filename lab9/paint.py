import pygame

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint App")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Default settings
selected_color = BLACK
drawing = False
mode = "free"  # Default mode (can be "square", "triangle", etc.)
start_pos = None

# Function to draw a right triangle
def draw_right_triangle(start, end):
    pygame.draw.polygon(screen, selected_color, [start, (end[0], start[1]), end])

# Function to draw an equilateral triangle
def draw_equilateral_triangle(start, end):
    base = end[0] - start[0]
    height = base * (3 ** 0.5) / 2
    pygame.draw.polygon(screen, selected_color, [start, (end[0], start[1]), (start[0] + base / 2, start[1] - height)])

# Function to draw a rhombus
def draw_rhombus(start, end):
    width = abs(end[0] - start[0])
    height = abs(end[1] - start[1])
    pygame.draw.polygon(screen, selected_color, [
        (start[0], start[1] + height // 2),
        (start[0] + width // 2, start[1]),
        (start[0] + width, start[1] + height // 2),
        (start[0] + width // 2, start[1] + height)
    ])

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)  # Refresh screen each frame

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                screen.fill(WHITE)  # Clear screen
            elif event.key == pygame.K_1:
                mode = "square"
            elif event.key == pygame.K_2:
                mode = "right_triangle"
            elif event.key == pygame.K_3:
                mode = "equilateral_triangle"
            elif event.key == pygame.K_4:
                mode = "rhombus"
            elif event.key == pygame.K_e:
                mode = "eraser"
            elif event.key == pygame.K_r:
                selected_color = RED
            elif event.key == pygame.K_g:
                selected_color = GREEN
            elif event.key == pygame.K_b:
                selected_color = BLUE
            elif event.key == pygame.K_k:
                selected_color = BLACK

        elif event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = event.pos
            drawing = True

        elif event.type == pygame.MOUSEBUTTONUP:
            end_pos = event.pos
            drawing = False

            if mode == "square":
                pygame.draw.rect(screen, selected_color, (*start_pos, end_pos[0] - start_pos[0], end_pos[0] - start_pos[0]))
            elif mode == "right_triangle":
                draw_right_triangle(start_pos, end_pos)
            elif mode == "equilateral_triangle":
                draw_equilateral_triangle(start_pos, end_pos)
            elif mode == "rhombus":
                draw_rhombus(start_pos, end_pos)
            elif mode == "eraser":
                pygame.draw.circle(screen, WHITE, end_pos, 20)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
