# Crossing Capstone

Welcome to Crossing Capstone, a thrilling turtle-based game where you guide a turtle through a busy street, avoiding oncoming cars and striving to reach higher levels.

## Game Overview

Crossing Capstone challenges you to navigate a turtle safely across a bustling street filled with speeding cars. As you progress through levels, the game becomes more difficult, increasing the speed and density of oncoming traffic.

## How to Play

- Control your turtle using the 'Up' arrow key to move forward.
- Dodge oncoming cars to safely cross the road.
- Each successful crossing increases your level, making the game more challenging.
- Be cautious! Colliding with a car ends the game.

## Game Elements

### Cars

- Cars move horizontally across the screen at varying speeds.
- Dodge the cars to avoid collisions.

### Levels

- The game features multiple levels.
- Each level increases the speed of oncoming cars.

### Player (Turtle)

- The player controls a turtle, navigating it through the busy street.
- Move forward using the 'Up' arrow key.

### Scoreboard

- The scoreboard displays your current level.
- Successfully crossing the road increases your level.
- The game ends if your turtle collides with a car.

## Getting Started

1. Ensure you have Python installed on your machine.
2. Run the provided script:

    ```bash
    python crossing_capstone.py
    ```

3. Use the 'Up' arrow key to navigate your turtle and avoid oncoming cars.

## Game Constants

- `COLORS`: List of colors for car representation.
- `STARTING_MOVE_DISTANCE`: Initial speed of oncoming cars.
- `MOVE_INCREMENT`: Speed increment when leveling up.

## Classes

### `CarManager`

- Manages the creation and movement of cars.
- Randomly generates cars with different colors and positions.
- Speed increases with each level.

### `Scoreboard`

- Displays the current level on the screen.
- Updates the level when the player successfully crosses the road.
- Shows "GAME OVER" if the player collides with a car.

### `Player`

- Represents the player-controlled turtle.
- Moves forward with the 'Up' arrow key.
- Checks if the player has reached the finish line.

## Customization

Feel free to explore the code and customize the game to suit your preferences. Modify the colors, speeds, or add new features to enhance the gaming experience.

## Acknowledgments

This game was created as part of a coding project and serves as an enjoyable implementation of basic game mechanics. Have fun playing Crossing Capstone!

**Note:** Ensure that you have Python and the Turtle graphics library installed to run the game.
