import pygame
from pygame.locals import *

#Jon Goga

# Initialize the game
pygame.init()

# Set up the game window
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ping Pong")

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the ball properties
ball_radius = 10
ball_pos = [width // 2, height // 2]
ball_velocity = [3, 3]

# Set up the paddle properties
paddle_width, paddle_height = 10, 60
paddle_pos = [0, height // 2 - paddle_height // 2]
paddle_velocity = 5

# Game loop
running = True
clock = pygame.time.Clock()
game_over = False  # New variable to track game state

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Move the paddle
    keys = pygame.key.get_pressed()
    if keys[K_UP] and paddle_pos[1] > 0:
        paddle_pos[1] -= paddle_velocity
    if keys[K_DOWN] and paddle_pos[1] < height - paddle_height:
        paddle_pos[1] += paddle_velocity

    # Move the ball
    ball_pos[0] += ball_velocity[0]
    ball_pos[1] += ball_velocity[1]

    # Check for collisions with the walls
    if ball_pos[1] <= 0 or ball_pos[1] >= height - ball_radius:
        ball_velocity[1] = -ball_velocity[1]
    if ball_pos[0] <= 0:
        ball_velocity[0] = -ball_velocity[0]
    if ball_pos[0] >= width - ball_radius:
        ball_velocity[0] = -ball_velocity[0]

    # Check for collision with the paddle
    if ball_pos[0] <= paddle_pos[0] + paddle_width and paddle_pos[1] <= ball_pos[1] <= paddle_pos[1] + paddle_height:
        ball_velocity[0] = -ball_velocity[0]

    # Clear the screen
    screen.fill(BLACK)

    # Draw the ball
    pygame.draw.circle(screen, WHITE, ball_pos, ball_radius)

    # Draw the paddle
    pygame.draw.rect(screen, WHITE, (paddle_pos[0], paddle_pos[1], paddle_width, paddle_height))

    # Update the display
    pygame.display.flip()

    # Check if the game is over
    if ball_pos[0] < 0:
        game_over = True

    # Check if the game is over or restart
    if game_over:
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over", True, WHITE)
        text_rect = text.get_rect(center=(width // 2, height // 2))
        screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(2000)  # Wait for 2 seconds
        ball_pos = [width // 2, height // 2]
        game_over = False

    # Limit the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
