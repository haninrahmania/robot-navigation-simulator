import pygame

BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Robot:
    def __init__(self, start, cell_size):
        self.position = start
        self.cell_size = cell_size
        self.path = []
        self.step_index = 0

    def set_path(self, path):
        self.path = path
        self.step_index = 0

    def update(self):
        if self.path and self.step_index < len(self.path):
            self.position = self.path[self.step_index]
            self.step_index += 1

    def draw(self, screen):
        r, c = self.position
        rect = pygame.Rect(
            c * self.cell_size,
            r * self.cell_size,
            self.cell_size,
            self.cell_size
        )
        pygame.draw.rect(screen, BLUE, rect)

    def draw_path(self, screen):
        for node in self.path:
            r, c = node
            rect = pygame.Rect(
                c * self.cell_size,
                r * self.cell_size,
                self.cell_size,
                self.cell_size
            )
            pygame.draw.rect(screen, GREEN, rect)

    def reached_goal(self):
        return not self.path and self.current_position == self.goal_position
