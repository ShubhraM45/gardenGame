import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((135, 206, 235))  # sky blue
    pygame.draw.rect(screen, (101, 67, 33), (0, 360, 640, 120))  # soil
    pygame.display.flip()
    clock.tick(60)

pygame.quit()