import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.player = 1

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                pygame.draw.rect(screen, pygame.Color('black'), (
                    self.left + j * self.cell_size, self.top + i * self.cell_size, self.cell_size, self.cell_size))
                pygame.draw.rect(screen, pygame.Color('white'), (
                    self.left + j * self.cell_size, self.top + i * self.cell_size, self.cell_size, self.cell_size), 1)

                if self.board[i][j] == 2:
                    # нолик
                    pygame.draw.circle(screen, pygame.Color('red'),
                        (self.left + j * self.cell_size + self.cell_size // 2, self.top + i * self.cell_size, self.cell_size + self.cell_size // 2), self.cell_size // 2 - 2, 2)
                elif self.board[i][j] == 1:
                    # крестик
                    # линия чертится по 4 координатам
                    # доделать
                    pygame.draw.line(screen, pygame.Color('blue'), (
                        self.left + j * self.cell_size + 2, self.top + i * self.cell_size + 2, self.cell_size, self.cell_size), 2)
                    pygame.draw.line(screen, pygame.Color('blue'), (
                        self.left + j * self.cell_size + self.cell_size - 2, self.top + i * self.cell_size + self.cell_size - 2, self.cell_size,
                        self.cell_size), 2)

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        if self.left <= x <= self.width * self.cell_size + self.left \
                and self.top <= y <= self.height * self.cell_size + self.top:
            x_res = (x - self.left) // self.cell_size
            y_res = (y - self.top) // self.cell_size
            return (x_res + 1, y_res + 1)
        else:
            return None

    def on_click(self, cell_coords):
        if cell_coords:
            y, x = cell_coords
            x, y = x - 1, y - 1
            if cell_coords:
                if self.player % 2 == 0:
                    self.board[x][y] = 2
                else:
                    self.board[x][y] = 1


    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)
        self.player += 1


pygame.init()
size = 500, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Инициализация запуска')
# поле 5 на 7
board = Board(5, 7)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()
pygame.quit()
