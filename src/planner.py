import heapq
import math

class AStarPlanner:
    def __init__(self, grid):
        self.grid = grid
        self.open_set = []
        self.came_from = {}
        self.g_score = {}
        self.closed_set = set()
        self.start = None
        self.goal = None
        self.finished = False
        self.path = None

    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan

    def get_neighbors(self, node):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbors = []

        for dr, dc in directions:
            neighbor = (node[0] + dr, node[1] + dc)

            if self.grid.in_bounds(neighbor) and not self.grid.is_obstacle(neighbor):
                neighbors.append(neighbor)

        return neighbors

    def initialize(self, start, goal):
        self.start = start
        self.goal = goal
        self.open_set = []
        heapq.heappush(self.open_set, (0, start))

        self.came_from = {}
        self.g_score = {start: 0}
        self.closed_set = set()
        self.finished = False
        self.path = None

    def step(self):
        if not self.open_set or self.finished:
            return

        _, current = heapq.heappop(self.open_set)

        if current in self.closed_set:
            return

        self.closed_set.add(current)

        if current == self.goal:
            self.finished = True
            self.path = self.reconstruct_path(current)
            return

        for neighbor in self.get_neighbors(current):
            tentative_g = self.g_score[current] + 1

            if neighbor in self.closed_set:
                continue

            if neighbor not in self.g_score or tentative_g < self.g_score[neighbor]:
                self.came_from[neighbor] = current
                self.g_score[neighbor] = tentative_g
                f_score = tentative_g + self.heuristic(neighbor, self.goal)
                heapq.heappush(self.open_set, (f_score, neighbor))

    def reconstruct_path(self, current):
        path = [current]
        while current in self.came_from:
            current = self.came_from[current]
            path.append(current)
        path.reverse()
        return path
