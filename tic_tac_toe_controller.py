"""
Tic-tac-toe controller.
"""

from abc import ABC, abstractmethod

import random

from tic_tac_toe_board import TicTacToeBoard


class TicTacToeController(ABC):
    """
    Abstract base class to control a tic-tac-toe game

    Attributes:
        board: board object representing the model of tic-tac-toe game
    """

    def __init__(self, board):
        """
        Initializes an object of the TicTacToeController class

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
    def move(self):
        """
        Make a move in the game
        """


class TextController(TicTacToeController):
    """
    Class to control a game of tic-tac-toe through text

    Attributes:
        board: board object representing the model of tic-tac-toe game
    """

    def move(self):
        """
        Makes a tic-tac-toe move by prompting user input

        Raises:
            IndexError: Value input isn't doesn't have length of 3
            ValueError: The first a third value isn't an integer
        """
        try:
            move_input = input("Please enter your move in the form row col: ")
            row = int(move_input[0])
            col = int(move_input[2])
            self._board.mark(row, col)
        except (IndexError, ValueError):
            print("Invalid move entered. Please enter row col. Ex '1 2'")
            self.move()


class CPUControllerRandom(TicTacToeController):
    """
    Class to control a game of tic-tac-toe by playing optimally.

    Attributes:
        board: board object representing the model of tic-tac-toe game
    """

    def move(self):
        """
        Makes an optimal tic-tac-toe move using Minimax tree search.

        If multiple moves are equally optimable, it chooses between them
        randomly.
        """

        cpu_player = self._board.next_move()
        other_player = (
            TicTacToeBoard.player_2_mark
            if cpu_player == TicTacToeBoard.player_1_mark
            else TicTacToeBoard.player_1_mark
        )

        def minimax():
            """
            Minimax tree search to find an optimal move.

            Returns:
                int: Best possible score differential
                tuple (int, int): The row and column of the optimal move
            """
            if self._board.game_over():
                score = 0
                if self._board.check_win(cpu_player):
                    score = 1
                elif self._board.check_win(other_player):
                    score = -1

                return score, None

            if self._board.next_move() == cpu_player:
                best = -float("inf")
                best_move = []

                for row, col in self._valid_moves():
                    self._board.mark(row, col)
                    diff, _ = minimax()
                    if diff > best:
                        best = diff
                        best_move = [(row, col)]
                    if diff == best:
                        best_move.append((row, col))
                    self._board.unmark(row, col)

                return best, random.choice(best_move)

            else:
                best = float("inf")
                best_move = []

                for row, col in self._valid_moves():
                    self._board.mark(row, col)
                    diff, _ = minimax()
                    if diff < best:
                        best = diff
                        best_move = [(row, col)]
                    if diff == best:
                        best_move.append((row, col))
                    self._board.unmark(row, col)

                return best, random.choice(best_move)

        _, best_move = minimax()

        self._board.mark(best_move[0], best_move[1])

    def _valid_moves(self):
        """
        Helper function to find all possible moves.

        Returns:
            List(tuple[ints]): All possible moves in a list of tuples of row, cols
        """
        moves = []
        for row in range(3):
            for col in range(3):
                if self._board.get_square(row, col) == TicTacToeBoard.blank_mark:
                    moves.append((row, col))

        return moves
