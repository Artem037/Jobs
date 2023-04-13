import pygame

if __name__ == '__main__':
    pygame.init()
    a, n = input().split()
    if not (a.isdigit() and n.isdigit()) or int(a) % int(n) != 0:
        print('Неправильный формат ввода')
        pygame.quit()
    else:
        a, n = int(a), int(n)
        screen = pygame.display.set_mode((a, a))
        pygame.display.set_caption('Шахматная клетка')
        x = a // n
        while pygame.event.wait().type != pygame.QUIT:
            if n % 2 == 0:
                k = 0
            else:
                k = 1
            for i in range(n):
                if i > 0:
                    if n % 2 == 0:
                        if k:
                            k = 0
                        else:
                            k = 1
                for j in range(n):
                    if k:
                        color = pygame.Color('black')
                        k = 0
                    else:
                        color = pygame.Color('white')
                        k = 1
                    pygame.draw.rect(screen, color, (i * x, j * x, x, x))
            pygame.display.flip()
        pygame.quit()
