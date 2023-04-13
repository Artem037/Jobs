import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))
    pygame.display.set_caption('Шарики')
    v = 100
    screen2 = pygame.Surface(screen.get_size())
    clock = pygame.time.Clock()
    running = True
    circles = []
    while running:
        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                circles.append([x, y, -1, -1])

        # отрисовка и изменение свойств объектов
        screen.fill((0, 0, 0))
        for i in range(len(circles)):

            x, y, d1, d2 = circles[i]

            pygame.draw.circle(screen, (255, 255, 255), (x, y), 10)

            if x - 10 <= 0:
                circles[i] = [x, y, 1, d2]
            if x + 10 >= 800:
                circles[i] = [x, y, -1, d2]
            if y - 10 <= 0:
                circles[i] = [x, y, d1, 1]
            if y + 10 >= 400:
                circles[i] = [x, y, d1, -1]
        tick = clock.tick()
        for i in range(len(circles)):
            circles[i][0] += v * tick * circles[i][2] / 1000
            circles[i][1] += v * tick * circles[i][3] / 1000
        # обновление экрана
        pygame.display.flip()
    pygame.quit()
