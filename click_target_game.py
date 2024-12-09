import pygame
import random
import time

pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Aim Trainer")

# Colors for target and background
RED = (255, 0, 0)
WHITE = (255, 255, 255)

TARGET_RADIUS = 30

target_count = 0
start_time = time.time()

# Function to generate a random position for the target
def get_random_position():
    x = random.randint(TARGET_RADIUS, SCREEN_WIDTH - TARGET_RADIUS)
    y = random.randint(TARGET_RADIUS, SCREEN_HEIGHT - TARGET_RADIUS)
    return x, y

target_position = get_random_position()

running = True
while running:
    elapsed_time = time.time() - start_time

    # Checks if 60 seconds have passed
    if elapsed_time > 60:
        running = False
        continue

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            target_x, target_y = target_position
            # Check if the click is on the target
            distance = ((mouse_x - target_x) ** 2 + (mouse_y - target_y) ** 2) ** 0.5
            if distance <= TARGET_RADIUS:
                target_count += 1
                target_position = get_random_position()

    # Clear the screen
    screen.fill(WHITE)

    pygame.draw.circle(screen, RED, target_position, TARGET_RADIUS)

    pygame.display.flip()

# Display score
screen.fill(WHITE)
font = pygame.font.Font(None, 74)
text = font.render(f"Targets hit: {target_count}", True, RED)
text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
screen.blit(text, text_rect)
pygame.display.flip()


pygame.time.wait(5000)
pygame.quit()
