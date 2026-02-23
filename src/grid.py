import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

class Grid:
    def __init__(self, rows, cols, cell_size, obstacle_ratio=0.2):
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]
        self.generate_obstacles(obstacle_ratio)

    def generate_obstacles(self, obstacle_ratio):
        for r in range(self.rows):
            for c in range(self.cols):
                if random.random() < obstacle_ratio:
                    self.grid[r][c] = 1  # 1 means obstacle

    def is_obstacle(self, node):
        r, c = node
        return self.grid[r][c] == 1

    def in_bounds(self, node):
        r, c = node
        return 0 <= r < self.rows and 0 <= c < self.cols

    def draw(self, screen):
        for r in range(self.rows):
            for c in range(self.cols):
                rect = pygame.Rect(
                    c * self.cell_size,
                    r * self.cell_size,
                    self.cell_size,
                    self.cell_size
                )

                if self.grid[r][c] == 1:
                    pygame.draw.rect(screen, BLACK, rect)
                else:
                    pygame.draw.rect(screen, WHITE, rect)

                pygame.draw.rect(screen, GRAY, rect, 1)
