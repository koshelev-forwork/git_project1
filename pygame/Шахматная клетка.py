import pygame

try:
    a, n = input().split(' ')
    assert a.isdigit() and n.isdigit()
    pygame.init()
    size = int(a), int(a)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Шахматная доска')
    a, n = int(a), int(n)
    rect_size = a // n
    if n % 2 != 0:
        x = 0
        y = 0
        for i in range(1, n + 1):
            if i % 2 != 0:
                x += rect_size
                for j in range(1, (a // rect_size) // 2 + 1):
                    pygame.draw.rect(screen, pygame.Color('white'), (x, y, rect_size, rect_size))
                    x += rect_size * 2
                x = 0
                y += rect_size
            else:
                for j in range(1, (a // rect_size) // 2 + 2):
                    pygame.draw.rect(screen, pygame.Color('white'), (x, y, rect_size, rect_size))
                    x += rect_size * 2
                x = 0
                y += rect_size
    else:
        x = 0
        y = 0
        for i in range(1, n + 1):
            if i % 2 == 0:
                x += rect_size
                for j in range(1, (n // 2) + 1):
                    pygame.draw.rect(screen, pygame.Color('white'), (x, y, rect_size, rect_size))
                    x += rect_size * 2
                x = 0
                y += rect_size
            else:
                for j in range(1, (n // 2) + 1):
                    pygame.draw.rect(screen, pygame.Color('white'), (x, y, rect_size, rect_size))
                    x += rect_size * 2
                x = 0
                y += rect_size
    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.update()
    pygame.quit()
except AssertionError:
    print('Неправильный формат ввода')
