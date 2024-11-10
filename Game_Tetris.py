import pygame
import random

# Константы
WIDTH, HEIGHT = 1000, 800
BLOCK_SIZE = 30
COLUMNS, ROWS = WIDTH // BLOCK_SIZE, HEIGHT // BLOCK_SIZE
FPS = 10

# Задаем цвета
COLORS = [
    (0, 255, 255),  # Циан
    (0, 0, 255),    # Синий
    (255, 165, 0),  # Оранжевый
    (255, 255, 0),  # Желтый
    (0, 255, 0),    # Зеленый
    (255, 0, 0),    # Красный
    (128, 0, 128)   # Фиолетовый
]

# Описание фигур
SHAPES = [
    [[1, 1, 1, 1]],              # I
    [[1, 1], [1, 1]],            # O
    [[0, 1, 0], [1, 1, 1]],      # T
    [[1, 0, 0], [1, 1, 1]],      # L
    [[0, 0, 1], [1, 1, 1]],      # J
    [[1, 1, 0], [0, 1, 1]],      # S
    [[0, 1, 1], [1, 1, 0]]       # Z
]

class Block:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
        self.x = COLUMNS // 2 - len(shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

class Board:
    def __init__(self):
        self.grid = [[0] * COLUMNS for _ in range(ROWS)]

    def is_valid_position(self, block, adj_x=0, adj_y=0):
        for y, row in enumerate(block.shape):
            for x, cell in enumerate(row):
                if cell:
                    new_x = block.x + x + adj_x
                    new_y = block.y + y + adj_y
                    if new_x < 0 or new_x >= COLUMNS or new_y >= ROWS:
                        return False
                    if new_y >= 0 and self.grid[new_y][new_x]:
                        return False
        return True

    def add_block(self, block):
        for y, row in enumerate(block.shape):
            for x, cell in enumerate(row):
                if cell:
                    self.grid[block.y + y][block.x + x] = block.color

    def clear_lines(self):
        new_grid = [row for row in self.grid if any(not cell for cell in row)]
        lines_cleared = ROWS - len(new_grid)
        for _ in range(lines_cleared):
            new_grid.insert(0, [0] * COLUMNS)
        self.grid = new_grid
        return lines_cleared

class TetrisGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Тетрис')
        self.clock = pygame.time.Clock()
        self.board = Board()
        self.current_block = None
        self.next_block()
        self.running = True

    def next_block(self):
        shape = random.choice(SHAPES)
        color = random.choice(COLORS)
        self.current_block = Block(shape, color)
        if not self.board.is_valid_position(self.current_block):
            self.running = False

    def run(self):
        while self.running:
            self.screen.fill((0, 0, 0))
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(FPS)
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.move_block(-1)
                elif event.key == pygame.K_RIGHT:
                    self.move_block(1)
                elif event.key == pygame.K_DOWN:
                    self.drop_block()
                elif event.key == pygame.K_UP:
                    self.rotate_block()

    def move_block(self, dx):
        if self.board.is_valid_position(self.current_block, adj_x=dx):
            self.current_block.x += dx

    def drop_block(self):
        if self.board.is_valid_position(self.current_block, adj_y=1):
            self.current_block.y += 1
        else:
            self.board.add_block(self.current_block)
            self.board.clear_lines()
            self.next_block()

    def rotate_block(self):
        self.current_block.rotate()
        if not self.board.is_valid_position(self.current_block):
            self.current_block.rotate()
            self.current_block.rotate()
            self.current_block.rotate()

    def update(self):
        if self.board.is_valid_position(self.current_block, adj_y=1):
            self.current_block.y += 1
        else:
            self.board.add_block(self.current_block)
            self.board.clear_lines()
            self.next_block()

    def draw(self):
        for y, row in enumerate(self.board.grid):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(self.screen, cell, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

        for y, row in enumerate(self.current_block.shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(self.screen, self.current_block.color,
                                     ((self.current_block.x + x) * BLOCK_SIZE,
                                      (self.current_block.y + y) * BLOCK_SIZE,
                                      BLOCK_SIZE, BLOCK_SIZE))

# Запуск игры
if __name__ == "__main__":
    game = TetrisGame()
    game.run()
