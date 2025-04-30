"""
Tic-tac-toe game view.
"""

from abc import ABC, abstractmethod


class TicTacToeView(ABC):
    """
    Abstract base class to view a tic-tac-toe game

    Attributes:
        board: board object representing the model of tic-tac-toe game
    """

    def __init__(self, board):
        """
        Initializes an object of the TicTacToeView class

        Parameters:
            _board = instance of Board object
        """
        self._board = board

    @property
    def board(self):
        """
        Returns the current board object
        """
        return self._board

    @abstractmethod
    def draw(self):
        """
        Draws the gameboard
        """


class TextView(TicTacToeView):
    """
    Class to view a tic-tac-toe game using text

    Attributes:
        board: board object representing the model of tic-tac-toe game
    """

    def draw(self):
        """
        Prints the current state of the board
        """
        board_as_string = ""
        for i in range(3):
            board_as_string += "+-+-+-+\n"
            board_as_string += f"|{self._board.get_square(i, 0)}"
            board_as_string += f"|{self._board.get_square(i, 1)}"
            board_as_string += f"|{self._board.get_square(i, 2)}|\n"
        board_as_string += "+-+-+-+\n"
        if not self._board.game_over():
            board_as_string += f"It is now {self._board.next_move()}'s turn."
        print(board_as_string)
