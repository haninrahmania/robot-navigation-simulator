# Robot Navigation Simulator
This project investigates classical deterministic motion planning methods for autonomous mobile robots in structured environments. A grid-based configuration space is constructed, and A* search is applied to compute collision-free trajectories under obstacle constraints. The simulator is designed as a foundation for further research into trajectory control, dynamic environments, and probabilistic robotics.

## Objectives
- Implement classical path planning algorithms used in robotics
- Model obstacle-aware navigation in a structured environment
- Visualize search behavior and trajectory execution
- Build a foundation for future extensions including control systems and dynamic environments

## Core Features
- 2D grid world representation
- Static obstacle placement
- A* path planning
- Path cost computation (g, h, f evaluation)
- Visualized search exploration and final trajectory
- Modular architecture separating environment, planner, and robot logic

## Technical Concepts
This project explores several fundamental robotics topics:
- Graph search and heuristic-based planning
- Configuration space modeling
- Discrete motion planning
- Autonomous navigation logic

## Future Extensions
- PID-based trajectory tracking
- Dynamic obstacle avoidance
- Probabilistic occupancy grid mapping
- Sensor noise simulation
- Multi-agent navigation
- Integration with ROS2

## Project Development Log
### Version 0.1.0 - Static Grid Navigation
#### Features:
- 2D grid world
- Static obstacle generation
- A* path planning (4-connected)
- Manhattan heuristic
- Path visualization
- Basic robot traversal

#### Limitations:
- No search exploration visualization
- Discrete teleport-style motion
- No dynamic obstacles
- No continuous trajectory modeling

### Version 0.2.0 - Incremental A* Execution & Search Visualization
#### Major Changes:
- Refactored A* implementation to support step-wise execution
- Exposed open set and closed set states
- Integrated real-time visualization of search expansion
- Converted planning loop from batch computation to incremental updates

#### Why This Matters:
- Improves transparency of algorithm behavior
- Enables debugging and heuristic analysis
- Establishes foundation for comparative planner experiments

#### New Limitations:
- Still limited to 4-connected grid
- Uniform cost movement
- No diagonal motion
- No continuous trajectory modeling

### Version 0.3.0 - 8-Connected A* Navigation
This update improves the navigation system by upgrading the motion model and heuristic for more realistic robot movement.

#### Motion Model Upgrade
The planner now uses an 8-connected grid instead of a 4-connected grid.

Previous (v0.2):
- Movement allowed: up, down, left, right
- Cost per move: 1

Current (v0.3):
- Movement allowed: up, down, left, right + 4 diagonals
- Cost:
-- 1 for cardinal moves
-- √2 for diagonal moves

This better approximates real-world robot motion and produces shorter, more natural paths.

#### Heuristic Update
The heuristic function has been upgraded from Manhattan distance to Euclidean distance.

Previous heuristic (Manhattan):

[ |x1 - x2| + |y1 - y2| ]

Current heuristic (Euclidean):

[ sqrt((x1 - x2)^2 + (y1 - y2)^2)] 

Euclidean distance is admissible and consistent for an 8-connected weighted grid, ensuring:
- Optimal paths
- Efficient node expansion
- Better geometric alignment with diagonal motion

This results in more realistic trajectories, shorter path length, reduced “staircase” effect, and better approximation of continuous-space navigation

### Version 0.4.0 -- 0.5.0 - Stable Interactive Navigation System

This update finalizes the A* implementation and upgrades the simulator into a fully interactive, reusable navigation system.

The focus of this release is algorithm stability, lifecycle management, and improved environment representation.

#### Search Termination & Stability Improvements

A critical edge-case was resolved in the A* search process.

Previous behavior (v0.3):
- The planner terminated only when the goal was reached.
- If no valid path existed, the open set would become empty.
- The algorithm failed to mark itself as finished.

This caused the simulation loop to continue indefinitely and prevented proper failure reporting.

Current behavior (v0.4):
- The planner explicitly detects an empty open set.
- Search now terminates correctly when no solution exists.
- Failure state is properly reported without freezing the simulation.

Result:
- Stable algorithm lifecycle
- Correct handling of impossible paths
- No infinite update loops

#### Planner Lifecycle Management
The planner is now reusable without restarting the program.

Added:
- reset(start, goal) method
- Full internal state reinitialization:
-- open set
-- closed set
-- g-score map
-- path state
-- finished flag

This allows:
- Multiple planning queries in a single run
- Dynamic replanning
- Clean simulation resets

#### Interactive Simulation Controls
The simulator now supports real-time interaction through mouse inputs.

Controls:
- Left Click → Set new goal position
- Right Click → Set new start position
- Middle Click → Regenerate map

Each interaction:
- Resets planner state
- Resets robot state
- Replans automatically

This transforms the project from a static demo into an interactive planning sandbox.

#### Obstacle Inflation & Configuration Space Visualization
Obstacle inflation was improved to better represent robot clearance.

Improvements:
- Inflated cells stored separately from real obstacles
- Visual differentiation between obstacle types

Grid representation:
- 0 → Free space (white)
- 1 → Real obstacles (black)
- 2 → Inflated safety buffer (dark grey)

Planner behavior:
- Both real and inflated obstacles are treated as non-traversable.
- The robot can only move through free cells.
- This introduces a clearer approximation of configuration-space planning.

#### Result

Version 0.5.0 represents a major system milestone:
- Stable A* implementation
- Proper success and failure termination
- Reusable planner lifecycle
- Interactive replanning
- Configuration-space obstacle inflation
- Clear visual separation of environment layers

The simulator now behaves as a fully interactive navigation prototype rather than a single-run pathfinding demo.