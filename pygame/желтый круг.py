import pygame
import random

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Жёлтый круг')
    size = w, h = random.randint(200, 700), random.randint(200, 700)
    screen = pygame.display.set_mode(size)
    screen.fill('blue')
    rad = 0
    radius_plus = pygame.USEREVENT + 1
    pygame.time.set_timer(radius_plus, 1000)

    running = True
    drawing = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                drawing = True
                screen.fill('blue')
                rad = 0
                cords = event.pos
            if event.type == radius_plus and drawing:
                rad += 10
                screen.fill('blue')
                pygame.draw.circle(screen, pygame.Color('yellow'), cords, rad)
        pygame.display.flip()
    pygame.quit()
