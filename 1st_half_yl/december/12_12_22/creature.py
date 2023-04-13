import os
import sys

import pygame

# Изображение не получится загрузить
# без предварительной инициализации pygame
pygame.init()
size = width, height = 300, 300
screen = pygame.display.set_mode(size)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


all_sprites = pygame.sprite.Group()

# создадим спрайт
sprite = pygame.sprite.Sprite()
# определим его вид
sprite.image = load_image("creature.png")
# и размеры
sprite.rect = sprite.image.get_rect()
# добавим спрайт в группу
all_sprites.add(sprite)

clock = pygame.time.Clock()
x, y = 0, 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                x, y = x, y - 10
            if event.key == pygame.K_DOWN:
                x, y = x, y + 10
            if event.key == pygame.K_RIGHT:
                x, y = x + 10, y
            if event.key == pygame.K_LEFT:
                x, y = x - 10, y

        sprite.rect.x = x
        sprite.rect.y = y

        screen.fill(pygame.Color('white'))
        all_sprites.draw(screen)
        all_sprites.update()
        clock.tick(30)
        pygame.display.flip()

pygame.quit()
