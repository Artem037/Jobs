import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    x_pos = 0
    k = 0
    v = 500
    fps = 60
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
                if not k:
                    k = 1
                elif k:
                    k = 0

        # отрисовка и изменение свойств объектов
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, (255, 0, 0), (x_pos, 200), 20)
        if not k:
            if x_pos >= 800:
                x_pos = 0
            else:
                x_pos += v / fps
                clock.tick(fps)

        # обновление экрана
        pygame.display.flip()
    pygame.quit()
