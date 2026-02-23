import pygame
from src.grid import Grid
from src.planner import AStarPlanner
from src.robot import Robot

ROWS = 20
COLS = 20
CELL_SIZE = 30
WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Robot Navigation Simulator")

    clock = pygame.time.Clock()

    grid = Grid(ROWS, COLS, CELL_SIZE, obstacle_ratio=0.2)

    start = (0, 0)
    goal = (ROWS - 1, COLS - 1)

    # Ensure start and goal are free
    grid.grid[start[0]][start[1]] = 0
    grid.grid[goal[0]][goal[1]] = 0

    planner = AStarPlanner(grid)
    path = planner.plan(start, goal)

    robot = Robot(start, CELL_SIZE)

    if path:
        robot.set_path(path)
    else:
        print("No path found!")

    running = True
    while running:
        clock.tick(5)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        robot.update()

        screen.fill((255, 255, 255))
        grid.draw(screen)

        if path:
            robot.draw_path(screen)

        robot.draw(screen)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
