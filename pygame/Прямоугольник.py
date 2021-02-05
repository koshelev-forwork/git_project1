import pygame

try:
    w, h = input().split(' ')
    assert w.isdigit() and h.isdigit()
    pygame.init()
    size = int(w), int(h)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Прямоугольник')
    # pygame.draw.rect(screen, pygame.Color('red'), ((1, 1), (int(w) - 1, int(h) - 1)))
    pygame.draw.rect(screen, pygame.Color('red'), ((1, 1), (199, 199)))
    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.update()
    pygame.quit()
except AssertionError:
    print('Неправильный формат ввода')
