pip install pygame

import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Configuraciones del juego
WIDTH, HEIGHT = 600, 400
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 10
BALL_RADIUS = 10
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Configuraciones de la bola
ball_speed = [4, 4]
ball_position = [WIDTH // 2, HEIGHT // 2]

# Configuraciones de la paleta
paddle_position = [WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - PADDLE_HEIGHT - 10]
paddle_speed = 5

# Configuraciones de los ladrillos
brick_width, brick_height = 50, 20
brick_rows = 5
brick_cols = WIDTH // brick_width
bricks = [[random.choice([0, 1]) for _ in range(brick_cols)] for _ in range(brick_rows)]

# Configuraciones de la pantalla
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Atari Breakout")

# Función para dibujar la paleta
def draw_paddle():
    pygame.draw.rect(screen, WHITE, (paddle_position[0], paddle_position[1], PADDLE_WIDTH, PADDLE_HEIGHT))

# Función para dibujar la bola
def draw_ball():
    pygame.draw.circle(screen, WHITE, (int(ball_position[0]), int(ball_position[1])), BALL_RADIUS)

# Función para dibujar los ladrillos
def draw_bricks():
    for row in range(brick_rows):
        for col in range(brick_cols):
            if bricks[row][col] == 1:
                pygame.draw.rect(screen, WHITE, (col * brick_width, row * brick_height, brick_width, brick_height))

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_position[0] > 0:
        paddle_position[0] -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_position[0] < WIDTH - PADDLE_WIDTH:
        paddle_position[0] += paddle_speed

    ball_position[0] += ball_speed[0]
    ball_position[1] += ball_speed[1]

    # Verificar colisiones con las paredes
    if ball_position[0] <= 0 or ball_position[0] >= WIDTH:
        ball_speed[0] *= -1
    if ball_position[1] <= 0:
        ball_speed[1] *= -1

    # Verificar colisión con la paleta
    if (
        paddle_position[0] <= ball_position[0] <= paddle_position[0] + PADDLE_WIDTH
        and paddle_position[1] <= ball_position[1] + BALL_RADIUS
    ):
        ball_speed[1] *= -1

    # Verificar colisiones con los ladrillos
    for row in range(brick_rows):
        for col in range(brick_cols):
            if (
                bricks[row][col] == 1
                and col * brick_width <= ball_position[0] <= (col + 1) * brick_width
                and row * brick_height <= ball_position[1] <= (row + 1) * brick_height
            ):
                ball_speed[1] *= -1
                bricks[row][col] = 0

    screen.fill(BLUE)
    draw_paddle()
    draw_ball()
    draw_bricks()

    pygame.display.flip()
    pygame.time.Clock().tick(60)
