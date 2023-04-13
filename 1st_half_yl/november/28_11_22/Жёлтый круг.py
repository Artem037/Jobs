import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 255))
    pygame.display.set_caption('Желтый круг')
    v = 10
    k = 0
    r = 0
    clock = pygame.time.Clock()
    running = True
    while running:
        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                k = 1
                x, y = pygame.mouse.get_pos()
                r = 0

        # отрисовка и изменение свойств объектов
        if k:
            screen.fill((0, 0, 255))
            pygame.draw.circle(screen, (255, 237, 0), (x, y), r)
            r += v * clock.tick() / 1000

        # обновление экрана
        pygame.display.flip()
    pygame.quit()
