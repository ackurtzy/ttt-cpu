# Tic-Tac-Toe CPU

A command-line Tic-Tac-Toe game implemented in Python using object-oriented principles. This version supports gameplay between a human and a CPU that uses the Minimax algorithm to make optimal decisions.

## Features

- **Modular Architecture**: Separates game logic, user interface, and control flow across four clear modules.
- **CPU Opponent**: The CPU uses the Minimax algorithm to choose optimal moves with randomness to break ties between equally good options.
- **Text-Based Interaction**: Play the game in the terminal with a clear visual representation of the board.
- **Error Handling**: Input validation and basic error recovery for user moves.

## Code Structure

- `tic_tac_toe_board.py`: Implements the `TicTacToeBoard` class, which manages the game state, player turns, and win/draw conditions.
- `tic_tac_toe_controller.py`: Contains:
  - `TicTacToeController` abstract base class
  - `TextController`: handles user input from the terminal
  - `CPUController`: plays optimally using the Minimax algorithm
- `tic_tac_toe_game.py`: The entry point that sets up the board, controllers, and view, and runs the game loop.
- `tic_tac_toe_view.py`: Implements the text-based `TextView` class for printing the game board and turn messages.

## How to Play

By default, the game runs a match between:
- **Player 1 (X)**: CPU (Minimax)
- **Player 2 (O)**: Human (terminal input)

### Example

```text
+-+-+-+
| | | |
+-+-+-+
| | | |
+-+-+-+
| | | |
+-+-+-+
It is now O's turn.
Please enter your move in the form row col: 1 1
```

### Run the Game

1. Clone the repository:

   ```bash
   git clone https://github.com/ackurtzy/ttt-cpu.git
   cd ttt-cpu
   ```

2. Run the game:

   ```bash
   python tic_tac_toe_game.py
   ```

## Acknowledgments

The core code was originally developed as part of the [Software Design course at Olin College of Engineering](https://github.com/olincollege/softdes-2024-01). This version includes modifications to support a CPU opponent using Minimax in the `CPUController` class.
