import pygame
import random

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Я слежу за тобой!')
    screen = pygame.display.set_mode((200, 200))

    running = True
    col_actions = 1
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.VIDEOEXPOSE:
                screen.fill((0, 0, 0))
                font = pygame.font.Font(None, 100)
                num = font.render(f"{col_actions}", True, (255, 0, 0))
                num_x = 100 - num.get_width() // 2
                num_y = 100 - num.get_height() // 2
                screen.blit(num, (num_x, num_y))
                col_actions += 1
        pygame.display.flip()
    pygame.quit()
