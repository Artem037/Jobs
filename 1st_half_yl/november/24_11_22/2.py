import pygame

if __name__ == '__main__':
    pygame.init()
    w, n = input().split()
    if not (w.isdigit() and n.isdigit()):
        print('Неправильный формат ввода')
        pygame.quit()
    else:
        w, n = int(w), int(n) - 1
        x, y = w * n * 2, w * n * 2
        screen = pygame.display.set_mode((x, y))
        pygame.display.set_caption('Мишень')

        if n % 3 == 1:
            start_color = (255, 0, 0)
        elif n % 3 == 2:
            start_color = (0, 255, 0)
        else:
            start_color = (0, 0, 255)

        while pygame.event.wait().type != pygame.QUIT:
            for i in range(n - 1):

        pygame.quit()
