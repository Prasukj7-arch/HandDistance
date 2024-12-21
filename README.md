# Hand Distance Game

## Project Description

This project is a real-time hand distance tracking game using computer vision. It uses OpenCV and the `cvzone` HandTrackingModule to detect hand gestures and calculate the distance between fingers. The game challenges players to hit a moving target by adjusting the distance between their fingers. Sound effects and a countdown timer enhance the gameplay experience.

## Key Features

- **Hand Gesture Recognition**: Uses hand tracking to calculate the distance between fingers.
- **Real-time Interaction**: Player interacts with a moving target by changing the distance between their fingers.
- **Game Mechanics**: The player hits a target and earns points when the hand is at a specific distance.
- **Sound Effects**: Background music and sound effects are added for a fun gaming experience.
- **Calibration**: The distance is converted to centimeters using polynomial calibration.
- **Game Over**: Displays the score at the end of the game and offers the option to restart.

## Technologies Used

- **Python**: Programming language used for the application.
- **OpenCV**: For hand gesture recognition and real-time video processing.
- **cvzone**: For easy hand detection and interaction with the webcam feed.
- **Pygame**: For managing music and sound effects.
- **Mathematics**: Polynomial calibration for converting pixel distance to real-world centimeters.

## Setup Instructions

### Prerequisites

Before setting up the project, ensure you have the following installed:

- Python 3.x
- pip (Python package installer)

### Installing Dependencies

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/HandDistance.git
    cd HandDistance
    ```

2. Install the required dependencies:

    ```bash
    pip install opencv-python cvzone pygame numpy
    ```

### Running the Game

1. Place the sound files (`background.mp3` and `hit_sound.wav`) in the same directory as the script.

2. Run the game:

    ```bash
    python hand_distance_game.py
    ```

3. The game will open in a new window, and you can start playing by adjusting the distance between your fingers to hit the target.

4. To restart the game, press `R` on your keyboard.

### Controls

- **Hand Movements**: Adjust the distance between your fingers to interact with the target.
- **Press 'R'**: Restart the game after it ends.

## Game Logic

- The game calculates the distance between the thumb and index finger.
- Based on this distance, the game checks if the player's hand is within the target's range.
- When the player hits the target, the score increases, and the target's position changes.
- The game runs for a set duration (20 seconds), after which the score is displayed, and the player can restart the game.

## Troubleshooting

- **Camera Not Detected**: Ensure your webcam is connected and accessible.
- **Hand Detection Issues**: Make sure your hand is well-lit and within the camera frame.

## Acknowledgments

- **OpenCV**: For the computer vision capabilities.
- **cvzone**: For simplifying hand tracking and gesture recognition.
- **Pygame**: For sound management and adding music to the game.
