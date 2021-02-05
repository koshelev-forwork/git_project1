import pygame
try:
    w, h = input().split(' ')
    assert w.isdigit() and h.isdigit()
    pygame.init()
    size = int(w), int(h)
    surface = pygame.display.set_mode(size)
    pygame.display.set_caption('Крест')
    pygame.draw.line(surface, (255, 255, 255), (0, 0), (int(w), int(h)), width=5)
    pygame.draw.line(surface, (255, 255, 255), (0, int(h)), (int(w), 0), width=5)
    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.update()
    pygame.quit()
except AssertionError:
    print('Неправильный формат ввода')
