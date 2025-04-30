"""
Main program to set up and run a tic-tac-toe game.
"""

from tic_tac_toe_board import TicTacToeBoard
from tic_tac_toe_view import TextView
from tic_tac_toe_controller import TextController, CPUControllerRandom


def main():
    """
    Play a game of tic-tac-toe by prompting user input
    """
    board = TicTacToeBoard()
    view = TextView(board)
    player_one = CPUControllerRandom(board)
    player_two = TextController(board)
    for i in range(1, 10):
        view.draw()
        if i % 2 == 0:
            player_one.move()
        else:
            player_two.move()
        if board.check_win("X") or board.check_win("O"):
            if board.check_win("X"):
                winner = "X"
            else:
                winner = "O"
            print(f"{winner}'s win!")
            break

    view.draw()
    if not board.check_win("X") and not board.check_win("O"):
        print("The game is a draw")


if __name__ == "__main__":
    main()
