import pygame
try:
    w, n = input().split(' ')
    assert w.isdigit() and n.isdigit()
    pygame.init()
    cen_wn = int(w) * int(n)
    size = cen_wn * 2, cen_wn * 2
    surface = pygame.display.set_mode(size)
    pygame.display.set_caption('Мишень')
    if int(n) % 3 == 0:
        color = 'blue'
    elif int(n) % 3 == 1:
        color = 'red'
    else:
        color = 'green'
    for i in range(1, int(n) + 1):
        pygame.draw.circle(surface, pygame.Color(color), (int(w) * int(n), int(w) * int(n)),  cen_wn)
        cen_wn -= int(w)
        if color == 'green':
            color = 'red'
        elif color == 'blue':
            color = 'green'
        else:
            color = 'blue'
    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.update()
    pygame.quit()
except AssertionError:
    print('Неправильный формат ввода')