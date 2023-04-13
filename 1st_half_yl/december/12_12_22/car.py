import os
import sys

import pygame

pygame.init()
size = width, height = 600, 95
screen = pygame.display.set_mode(size)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


all_sprites = pygame.sprite.Group()


class Car(pygame.sprite.Sprite):
    image = load_image("car2.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = Car.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.x = 5

    def update(self):
        if self.rect.x + self.rect[2] >= 600:
            self.image = pygame.transform.flip(self.image, True, False)
            self.x = -5
        elif self.rect.x <= -1:  # если бы было self.rect.x <= 0, то в самом начале машина бы переворачивалась
            self.image = pygame.transform.flip(self.image, True, False)
            self.x = 5
        self.rect = self.rect.move(self.x, 0)


Car(all_sprites)

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(pygame.Color('white'))
    all_sprites.draw(screen)
    all_sprites.update()
    clock.tick(60)
    pygame.display.flip()

pygame.quit()
