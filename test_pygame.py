import pygame

pygame.init()

width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game Pygame đầu tiên")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

x, y = 280, 180
speed = 5

running = True
while running:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x -= speed
    if keys[pygame.K_d]:
        x += speed
    if keys[pygame.K_w]:
        y -= speed
    if keys[pygame.K_s]:
        y += speed
    if keys[pygame.K_x]:
        running = False

    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (x, y, 40, 40))
    pygame.display.update()

pygame.quit()
