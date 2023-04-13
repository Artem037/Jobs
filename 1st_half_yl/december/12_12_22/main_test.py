import os
import sys
import random

import pygame

# Изображение не получится загрузить
# без предварительной инициализации pygame
pygame.init()
size = width, height = 500, 500
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


all_sprites = pygame.sprite.Group()

# # создадим спрайт
# sprite = pygame.sprite.Sprite()
# # определим его вид
# sprite.image = load_image("bomb.png")
# # и размеры
# sprite.rect = sprite.image.get_rect()
# # добавим спрайт в группу
# all_sprites.add(sprite)
#
# sprite.rect.x = 5
# sprite.rect.y = 20
#
# bomb_image = load_image("bomb.png")
#
# for i in range(50):
#     # можно сразу создавать спрайты с указанием группы
#     bomb = pygame.sprite.Sprite(all_sprites)
#     bomb.image = bomb_image
#     bomb.rect = bomb.image.get_rect()
#
#     # задаём случайное местоположение бомбочке
#     bomb.rect.x = random.randrange(width)
#     bomb.rect.y = random.randrange(height)
#     all_sprites.draw(screen)
#     pygame.flip()

class Bomb(pygame.sprite.Sprite):
    image = load_image("bomb.png")
    image_boom = load_image("boom.png")

    def __init__(self, group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно !!!
        super().__init__(group)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width)
        self.rect.y = random.randrange(height)

    def update(self, *args):
        self.rect = self.rect.move(random.randrange(3) - 1,
                                   random.randrange(3) - 1)
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.image = self.image_boom


for _ in range(50):
    Bomb(all_sprites)

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        screen.fill(pygame.Color('white'))
        all_sprites.draw(screen)
        all_sprites.update(event)
        clock.tick(30)
        pygame.display.flip()

pygame.quit()