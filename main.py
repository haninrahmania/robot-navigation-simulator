import pygame
from src.grid import Grid
from src.planner import AStarPlanner
from src.robot import Robot

ROWS = 20
COLS = 20
CELL_SIZE = 30
WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE

WHITE = (255, 255, 255)
ORANGE = (255, 165, 0)   # Closed set
YELLOW = (255, 255, 0)   # Open set

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Robot Navigation Simulator")

    clock = pygame.time.Clock()

    grid = Grid(ROWS, COLS, CELL_SIZE, obstacle_ratio=0.1)

    start = (0, 0)
    goal = (ROWS - 1, COLS - 1)

    grid.inflate_obstacles(radius=1)

    # Ensure start and goal are free
    grid.grid[start[0]][start[1]] = 0
    grid.grid[goal[0]][goal[1]] = 0

    planner = AStarPlanner(grid)
    planner.reset(start, goal)


    robot = Robot(start, CELL_SIZE)

    running = True
    failure_reported = False

    while running:
        clock.tick(30) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:

                # mouse_x, mouse_y = pygame.mouse.get_pos()

                # col = mouse_x // CELL_SIZE
                # row = mouse_y // CELL_SIZE

                # # Safety check (inside grid bounds)
                # if 0 <= row < ROWS and 0 <= col < COLS:

                #     # Only allow clicking free cells
                #     if grid.grid[row][col] == 0:

                #         goal = (row, col)

                #         planner.reset(start, goal)
                #         robot = Robot(start, CELL_SIZE)

                #         failure_reported = False

                mouse_x, mouse_y = pygame.mouse.get_pos()

                col = mouse_x // CELL_SIZE
                row = mouse_y // CELL_SIZE

                if 0 <= row < ROWS and 0 <= col < COLS:

                    # LEFT CLICK → SET NEW GOAL
                    if event.button == 1:

                        if grid.grid[row][col] == 0:
                            goal = (row, col)

                            planner.reset(start, goal)
                            robot = Robot(start, CELL_SIZE)

                            failure_reported = False


                    # RIGHT CLICK → SET NEW START
                    elif event.button == 3:

                        if grid.grid[row][col] == 0:
                            start = (row, col)

                            planner.reset(start, goal)
                            robot = Robot(start, CELL_SIZE)

                            failure_reported = False


                    # MIDDLE CLICK → REGENERATE MAP
                    elif event.button == 2:

                        grid = Grid(ROWS, COLS, CELL_SIZE, obstacle_ratio=0.1)
                        grid.inflate_obstacles(radius=1)

                        # Ensure start & goal are free
                        grid.grid[start[0]][start[1]] = 0
                        grid.grid[goal[0]][goal[1]] = 0

                        planner = AStarPlanner(grid)
                        planner.reset(start, goal)

                        robot = Robot(start, CELL_SIZE)

                        failure_reported = False

        # STEP-BY-STEP PLANNING
        if not planner.finished:
            planner.step()

        elif planner.finished and planner.path is None and not failure_reported:
            print("No path found.")
            failure_reported = True
            
        elif planner.path and not robot.path:
            robot.set_path(planner.path)

        robot.update()

        screen.fill(WHITE)
        grid.draw(screen)

        # Draw closed set (explored nodes)
        for node in planner.closed_set:
            r, c = node
            rect = pygame.Rect(c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, ORANGE, rect)

        # Draw open set (frontier)
        for _, node in planner.open_set:
            r, c = node
            rect = pygame.Rect(c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, YELLOW, rect)

            
        # Draw final path if found
        if planner.path:
            robot.draw_path(screen)

        

        robot.draw(screen)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
