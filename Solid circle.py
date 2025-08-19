import pygame

pygame.init()
screen = pygame.display.set_mode((400,400))
done = False
screen.fill((255, 255, 255))

while not done:
    GREEN = (0, 255, 0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.circle(screen, GREEN, (300, 300), 50)
    pygame.draw.circle(screen, GREEN, (100, 100), 50, 3)
    pygame.display.update()
    running = True

    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

pygame.display.flip()