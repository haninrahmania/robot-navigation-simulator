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
### Version 1 - Static Grid Navigation
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

### Version 2 - Incremental A* Execution & Search Visualization
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
