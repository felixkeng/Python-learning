# WRITE YOUR SOLUTION HERE:
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
window_width, window_height = 400, 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Asteroid Collector")

# Load images
robot_image = pygame.image.load("robot.png")
rock_image = pygame.image.load("rock.png")

# Define colors
BLACK = (0, 0, 0)

# Robot settings
robot_width, robot_height = robot_image.get_size()
robot_x = (window_width - robot_width) // 2
robot_y = window_height - robot_height - 10

# Asteroid settings
rock_width, rock_height = rock_image.get_size()
rock_x = random.randint(0, window_width - rock_width)
rock_y = -rock_height
rock_speed = 5

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move robot left and right
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and robot_x > 0:
        robot_x -= 5
    if keys[pygame.K_RIGHT] and robot_x < window_width - robot_width:
        robot_x += 5

    # Move rock down
    rock_y += rock_speed

    # Check if rock is collected
    if (rock_y + rock_height > robot_y) and (rock_y < robot_y + robot_height) and (rock_x + rock_width > robot_x) and (rock_x < robot_x + robot_width):
        score += 1
        rock_y = -rock_height  # Reset rock to the top
        rock_x = random.randint(0, window_width - rock_width)  # Randomize x position

    # Check if rock is missed
    if rock_y > window_height:
        print("Game Over! Final Score:", score)
        running = False

    # Fill the background
    window.fill(BLACK)

    # Draw the robot and rock
    window.blit(robot_image, (robot_x, robot_y))
    window.blit(rock_image, (rock_x, rock_y))

    # Draw score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    window.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Frame rate
    pygame.time.delay(30)

# Quit Pygame
pygame.quit()
