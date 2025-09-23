# The Farmer Was Replaced

My solutions to coding challenges in "The Farmer Was Replaced" - a programming puzzle game where you write scripts to automate farming tasks, solve mazes, and complete various algorithmic challenges.

## Challenge Solutions

### `Main.py`

Main solution script that runs different farming challenges. Configures world parameters and executes the appropriate algorithm based on the current challenge mode.

### `Debug.py`

Performance testing solution that measures execution time and resource usage across multiple farming operations. Used to optimize algorithms and compare different approaches.

## Algorithm Solutions

### `Cactus.py`

Solution for cactus sorting challenge. Implements a bubble-sort-like algorithm using neighbor swapping to sort cactuses by value across the field grid.

### `Replant.py`

Solution for general crop farming challenges. Handles multiple crop types with different planting patterns, including special logic for pumpkin farming that requires multiple passes.

### `Poly.py`

Solution for polyculture farming challenge. Implements companion planting algorithm that arranges different crops in optimal patterns for maximum yield.

### `Maze.py`

Solution for treasure hunting puzzle. Creates mazes using "Weird Substance" and implements both simple spiral traversal and advanced pathfinding algorithms to find treasure.

## Specialized Challenges

### `Dinosaurs.py`

Solution for the dinosaur pattern challenge (snake game variant). Creates a specific movement pattern that traces a dinosaur shape across the field using hat changes and directional movement.

### `Repeatable.py`

Utility for running challenge solutions in loops, useful for testing and optimization.

## Utility Modules (`util/`)

### `FarmingChecks.py`

Helper functions for checking entity types and farming conditions during challenges.

### `FarmingUtils.py`

Core farming utilities including:

- Watering and fertilizing functions
- Tilling operations (single tile or entire field)
- Movement and navigation helpers

### `Helpers.py`

General utility functions including:

- Grid navigation and positioning
- Field grid creation and management
- Movement algorithms for efficient field traversal
- Backtracking for maze solving

## Challenge Types

The solutions cover various programming challenges:

- **Sorting Algorithms**: Cactus value sorting using neighbor swapping
- **Pathfinding**: Maze solving with multiple traversal strategies
- **Pattern Generation**: Dinosaur shape creation and movement
- **Grid Algorithms**: Efficient field traversal and crop management
- **Optimization**: Performance testing and algorithm comparison

## Usage

Run `Main.py` to execute the main challenge solution. Individual challenge files can be run separately to test specific algorithms.
