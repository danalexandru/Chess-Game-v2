"""
The part of the project that deals with the login between chess pieces
"""
import copy

import common
from piece import Rook, Knight, Bishop, Queen, King, Pawn, Empty


class Board(object):
    def __init__(self):
        self.rows = common.DIMENSION
        self.cols = common.DIMENSION

        self.current_color = "white"

        self.king_position = {
            "black": (0, 4),
            "white": (7, 4)
        }

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

        self.special_moves_cases(last_position, next_position)
        self.board_inst[next_row, next_col] = self.board_inst[last_row, last_col]
        self.board_inst[last_row, last_col] = Empty(last_row, last_col, None)

        self.board_inst[next_row, next_col].move(next_row, next_col)

    def update_valid_moves(self):
        """
        This method updated the valid moves list of all chess pieces across the board

        :return: None
        """
        for row in range(self.rows):
            for col in range(self.cols):
                self.board_inst[row, col].update_valid_moves(self.board_inst)

    def filter_valid_moves(self):
        """
        This method filters the valid moves list of all chess pieces across the board (in case of check)

        :return: None
        """
        def remove_invalid_moves(board_inst, current_piece):
            temp_board = Board()
            temp_board.board_inst = copy.deepcopy(board_inst)
            temp_board.current_color = current_piece.color

            for (valid_row, valid_col) in current_piece.valid_moves:
                temp_board.move((current_piece.row, current_piece.col), (valid_row, valid_col))
                temp_board.get_piece((valid_row, valid_col)).update_valid_moves(temp_board.board_inst)

                dict_is_check = temp_board.is_in_check()
                if dict_is_check["black"] or dict_is_check["white"]:
                    current_piece.valid_moves.remove((valid_row, valid_col))

            del temp_board

        for row in range(self.rows):
            for col in range(self.cols):
                if isinstance(self.board_inst[row, col], Empty):
                    continue

                if (row, col) in [self.king_position["black"], self.king_position["white"]]:
                    continue

                piece = self.get_piece((row, col))
                remove_invalid_moves(self.board_inst, piece)

    def is_move_valid(self, last_position, next_position):
        """
        This method validated the current move that is being made

        :param last_position: (Integer, Integer) The last position of the selected chess piece
        :param next_position: (Integer, Integer) The next position of the selected chess piece
        :return: Boolean (True or False)
        """
        (last_row, last_col) = last_position
        (next_row, next_col) = next_position

        self.board_inst[last_row, last_col].update_valid_moves(self.board_inst)
        if self.board_inst[last_row, last_col].is_selected and \
                self.board_inst[last_row, last_col].validate_move(next_row, next_col):
            return True

        return False

    def update_current_color(self):
        """
        This method update the color of the current player

        :return: None
        """
        if self.current_color == "black":
            self.current_color = "white"
        elif self.current_color == "white":
            self.current_color = "black"
        else:
            common.error("Unrecognized color: \"%s\". Exit game." % str(self.current_color))

    def special_moves_cases(self, last_position, next_position):
        """
        This method tackles special moves such as "castling" or "en passant"

        :param last_position: (Integer, Integer) The last position of the selected chess piece
        :param next_position: (Integer, Integer) The next position of the selected chess piece
        :return: None
        """
        (last_row, last_col) = last_position
        (next_row, next_col) = next_position

        # check for king's side castling
        if isinstance(self.board_inst[last_row, last_col], King) and \
                isinstance(self.board_inst[last_row, 7], Rook) and \
                self.board_inst[last_row, last_col].has_been_moved is False and \
                self.board_inst[last_row, 7].has_been_moved is False and \
                next_row == last_row and next_col == 6:
            # king_side_castling = True
            self.board_inst[last_row, 7].move(last_row, 5)
            self.board_inst[last_row, 5] = self.board_inst[last_row, 7]
            self.board_inst[last_row, 7] = Empty(last_row, 7, None)

        # check for queen's side castling
        if isinstance(self.board_inst[last_row, last_col], King) and \
                isinstance(self.board_inst[last_row, 0], Rook) and \
                self.board_inst[last_row, last_col].has_been_moved is False and \
                self.board_inst[last_row, 0].has_been_moved is False and \
                next_row == last_row and next_col == 2:
            # queen_side_castling = True
            self.board_inst[last_row, 0].move(last_row, 3)
            self.board_inst[last_row, 3] = self.board_inst[last_row, 0]
            self.board_inst[last_row, 0] = Empty(last_row, 7, None)

        # reset special pawn case: en passant
        for i in range(self.rows):
            for j in range(self.cols):
                if isinstance(self.board_inst[i, j], Pawn) and \
                        self.board_inst[i, j].color == self.current_color:
                    self.board_inst[i, j].initial_move = False

        # special pawn case (first move)
        if isinstance(self.board_inst[last_row, last_col], Pawn) and \
                self.board_inst[last_row, last_col].initial_position is True and \
                abs(next_row - last_row) == 2:
            self.board_inst[last_row, last_col].initial_move = True

        # special case: en passant
        if isinstance(self.board_inst[last_row, last_col], Pawn) and \
                isinstance(self.board_inst[next_row, next_col], Empty) and \
                isinstance(self.board_inst[last_row, next_col], Pawn) and \
                self.board_inst[last_row, next_col].color != self.board_inst[last_row, last_col].color and \
                abs(next_col - last_col) == 1:
            # self.score[self.board_inst[last_row, last_col].color] += self.board_inst[last_row, next_col].strength
            self.board_inst[last_row, next_col] = Empty(last_row, next_col, None)

        # replace Pawn with Queen
        if next_row == 0 and isinstance(self.board_inst[next_row, next_col], Pawn) and \
                self.board_inst[next_row, next_col].color == 'white':
            self.board_inst[next_row, next_col] = Queen(next_row, next_col, 'white')

        if next_row == 7 and isinstance(self.board_inst[next_row, next_col], Pawn) and \
                self.board_inst[next_row, next_col].color == 'black':
            self.board_inst[next_row, next_col] = Queen(next_row, next_col, 'black')

    def update_king_position(self, last_position, next_position):
        """
        This method updates the last position of the King (if the King was moved)

        :param last_position: (Integer, Integer) The last position of the King
        :param next_position: (Integer, Integer) The next position of the King
        :return: None
        """
        if last_position != self.king_position["black"] and next_position != self.king_position["white"]:
            return
        elif last_position == self.king_position["black"]:
            self.king_position["black"] = next_position
        else:
            self.king_position["white"] = next_position

    def is_in_check(self):
        """
        This method determines whether or not either King is in check

        :return: (Dict) A dictionary containing whether or not a King is in check
        {
            "black": <Boolean>,
            "white": <Boolean>
        }
        """
        self.update_valid_moves()

        dict_result = {
            "black": False,
            "white": False
        }

        for row in range(self.rows):
            for col in range(self.cols):
                if (row, col) in [self.king_position["black"], self.king_position["white"]]:
                    continue

                piece = self.get_piece((row, col))
                if self.king_position["black"] in piece.valid_moves and piece.color == "white":
                    dict_result["black"] = True

                if self.king_position["white"] in piece.valid_moves and piece.color == "black":
                    dict_result["white"] = True

        return dict_result
