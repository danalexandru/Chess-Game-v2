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