import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 50
ENEMY_SIZE = 50
BULLET_SIZE = 10
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Player
player = pygame.Rect(WIDTH // 2 - PLAYER_SIZE // 2, HEIGHT - 2 * PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE)

# Enemies
enemies = []
for _ in range(5):
    enemy = pygame.Rect(random.randint(0, WIDTH - ENEMY_SIZE), random.randint(50, 300), ENEMY_SIZE, ENEMY_SIZE)
    enemies.append(enemy)

# Bullets
bullets = []

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    player_speed = 5

    # Move player
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += player_speed

    # Shoot bullets
    if keys[pygame.K_SPACE]:
        bullet = pygame.Rect(player.centerx - BULLET_SIZE // 2, player.y - BULLET_SIZE, BULLET_SIZE, BULLET_SIZE)
        bullets.append(bullet)

    # Move bullets
    bullets = [bullet for bullet in bullets if bullet.y > 0]
    for bullet in bullets:
        bullet.y -= 10

    # Move enemies
    for enemy in enemies:
        enemy.y += 2

        # Check collisions with bullets
        for bullet in bullets:
            if enemy.colliderect(bullet):
                enemies.remove(enemy)
                bullets.remove(bullet)
                new_enemy = pygame.Rect(random.randint(0, WIDTH - ENEMY_SIZE), random.randint(50, 300), ENEMY_SIZE, ENEMY_SIZE)
                enemies.append(new_enemy)

    # Check collisions with player
    if any(enemy.colliderect(player) for enemy in enemies):
        print("Game Over!")
        pygame.quit()
        sys.exit()

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, player)

    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    for bullet in bullets:
        pygame.draw.rect(screen, BLUE, bullet)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(FPS)
