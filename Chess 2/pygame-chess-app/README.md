# Pygame Chess Application

This is a modern, intuitive chess application built using Pygame. The application allows users to play chess locally with a clean user interface and various features.

## Features

- **Piece Movement**: Move chess pieces according to standard chess rules.
- **Undo Functionality**: Easily undo the last move to correct mistakes.
- **Clean User Interface**: A visually appealing interface for an enjoyable gaming experience.

## Project Structure

```
pygame-chess-app
├── src
│   ├── main.py          # Entry point of the application
│   ├── chess
│   │   ├── board.py     # Chessboard representation and move validation
│   │   ├── pieces.py    # Definitions for chess pieces and their movements
│   │   ├── game.py      # Game logic, turn management, and undo functionality
│   │   └── utils.py     # Utility functions for loading images and checking moves
│   ├── ui
│   │   ├── renderer.py   # Rendering the chessboard and pieces
│   │   └── buttons.py    # Button classes for user interactions
│   └── assets
│       └── __init__.py   # Empty initializer for assets directory
├── requirements.txt      # Project dependencies
└── README.md             # Documentation for the project
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd pygame-chess-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python src/main.py
   ```

## Usage

- Launch the application and start a new game.
- Click on pieces to select and move them according to chess rules.
- Use the undo button to revert the last move if needed.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.