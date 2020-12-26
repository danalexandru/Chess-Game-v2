"""
The part of the project that deals with the login between chess pieces
"""
import common
from piece import Rook, Knight, Bishop, Queen, King, Pawn, Empty


class Board(object):
    def __init__(self):
        self.rows = common.DIMENSION
        self.cols = common.DIMENSION

        self.current_color = "white"

        self.board_inst = {}
        for row in range(self.rows):
            for col in range(self.cols):
                self.board_inst[row, col] = Empty(row, col, None)

        self.board_inst[0, 0] = Rook(0, 0, 'black')
        self.board_inst[0, 1] = Knight(0, 1, 'black')
        self.board_inst[0, 2] = Bishop(0, 2, 'black')
        self.board_inst[0, 3] = Queen(0, 3, 'black')
        self.board_inst[0, 4] = King(0, 4, 'black')
        self.board_inst[0, 5] = Bishop(0, 5, 'black')
        self.board_inst[0, 6] = Knight(0, 6, 'black')
        self.board_inst[0, 7] = Rook(0, 7, 'black')

        self.board_inst[7, 0] = Rook(7, 0, 'white')
        self.board_inst[7, 1] = Knight(7, 1, 'white')
        self.board_inst[7, 2] = Bishop(7, 2, 'white')
        self.board_inst[7, 3] = Queen(7, 3, 'white')
        self.board_inst[7, 4] = King(7, 4, 'white')
        self.board_inst[7, 5] = Bishop(7, 5, 'white')
        self.board_inst[7, 6] = Knight(7, 6, 'white')
        self.board_inst[7, 7] = Rook(7, 7, 'white')

        for i in range(common.DIMENSION):
            self.board_inst[1, i] = Pawn(1, i, 'black')
            self.board_inst[6, i] = Pawn(6, i, 'white')

    def select(self, position):
        """
        This function selects the current chess piece that was clicked on

        :param position: The position of the chess piece on the board
        :return: Boolean (True or False
        """
        (row, col) = position
        if not isinstance(self.board_inst[row, col], Empty) and \
                self.board_inst[row, col].color == self.current_color:
            self.board_inst[row, col].select()

    def cancel(self):
        """
        This method cancels the previous selection

        :return: None
        """
        for row in range(self.rows):
            for col in range(self.cols):
                self.board_inst[row, col].cancel()

    def get_piece(self, position):
        """
        This method returns the chess piece at the requested position

        :param position: The position of the chess piece on the board
        :return: (Piece) The chess piece
        """
        (row, col) = position
        return self.board_inst[row, col]

    def move(self, last_position, next_position):
        """
        This method moves the selected chess piece from the last position to the next one
        :param last_position: (Integer, Integer) The last position of the selected chess piece
        :param next_position: (Integer, Integer) The next position of the selected chess piece
        :return: None
        """
        if last_position == next_position:
            return

        (last_row, last_col) = last_position
        (next_row, next_col) = next_position

        self.board_inst[next_row, next_col] = self.board_inst[last_row, last_col]
        self.board_inst[last_row, last_col] = Empty(last_row, last_col, None)

        self.board_inst[next_row, next_col].move(next_row, next_col)

    def is_move_valid(self, last_position, next_position):
        """
        This method validated the current move that is being made
        :param last_position: (Integer, Integer) The last position of the selected chess piece
        :param next_position: (Integer, Integer) The next position of the selected chess piece
        :return: Boolean (True or False)
        """
        # TODO add logic for last_position and next_position
        (last_row, last_col) = last_position
        if self.board_inst[last_row, last_col].is_selected:
            return True

        return False
