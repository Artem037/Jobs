import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))
    pygame.display.set_caption('Перетаскивание')
    running = True
    x1, y1 = 50, 50
    x2, y2 = 0, 0
    drawing = False
    while running:
        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                x -= x2
                y -= y2
                if not (0 <= x <= 100 and 0 <= y <= 100):
                    drawing = False
                    print(1)
                else:
                    drawing = True
            if event.type == pygame.MOUSEBUTTONUP:
                if drawing:
                    drawing = False
                    x2, y2 = x1 - x, y1 - y
            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    x1, y1 = event.pos

        # отрисовка и изменение свойств объектов
        if x1 == 50 and y1 == 50:
            pygame.draw.rect(screen, (0, 255, 0), ((x1 - 50, y1 - 50), (100, 100)))
        if drawing:
            screen.fill(pygame.Color('black'))
            pygame.draw.rect(screen, (0, 255, 0), ((x1 - x, y1 - y), (100, 100)))
        # обновление экрана
        pygame.display.flip()
    pygame.quit()
