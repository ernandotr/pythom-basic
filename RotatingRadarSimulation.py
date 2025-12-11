import pygame, math

pygame.init()

screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
angle = 0
running = True

while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    pygame.draw.circle(screen, (0, 255, 0), (250, 250), 100, 2)
    x = 250 + 100 * math.cos(angle)
    y = 250 + 100 * math.sin(angle)
    pygame.draw.line(screen, (0, 255, 0), (250, 250), (x, y), 2)
    angle += 0.05
    pygame.display.flip()
    clock.tick(60)  
pygame.quit()
