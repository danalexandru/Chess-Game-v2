"""
The part of the project that deals with the logic of individual chess pieces
"""
# region imports
import copy
# endregion imports


# region Piece
class Piece(object):
    name = ""
    short_name = ""
    is_selected = False
    strength = 0
    valid_moves = []

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def move(self, row, col):
        """
        This method updates the position of the current chess piece

        :param row: (Integer) The updated row value
        :param col: (Integer) The updated column value
        :return: None
        """
        self.row = row
        self.col = col

    def select(self):
        """
        This method selects the current chess piece
        :return: None
        """
        self.is_selected = True

    def cancel(self):
        """
        This method cancels a previous selection
        :return: None
        """
        self.is_selected = False

    def clear_valid_moves(self):
        """
        This method resets the valid moves list of the current piece

        :return: None
        """
        self.valid_moves = []

    def validate_move(self, row, col):
        """
        This method determines whether the next position is valid or not

        :param row: (Integer) the possible next row position
        :param col: (Integer) the possible next column position
        :return:  Boolean(True of False)
        """
        if (row, col) in self.valid_moves:
            return True

        return False

    def update_valid_moves(self, board_inst):
        """
        This method updated the list of valid moves of the current chess piece

        :param board_inst: (Dict{8, 8}) The current state of the chess pieces on the board
        :return: None
        """
        pass

# endregion Piece


# region Rook
class Rook(Piece):
    name = "Rook"
    short_name = "R"
    strength = 5
    has_been_moved = False

    def update_valid_moves(self, board_inst):
        """
        This method updated the list of valid moves of the current chess piece

        :param board_inst: (Dict{8, 8}) The current state of the chess pieces on the board
        :return: None
        """
        self.clear_valid_moves()

        i = self.row
        j = self.col

        def list_directions():
            return [[-1, 0], [0, -1], [1, 0], [0, 1]]

        for direction in list_directions():
            [x, y] = [i + direction[0], j + direction[1]]

            while True:
                if (x < 0 or x > 7) or \
                        (y < 0 or y > 7):
                    break

                possible_next_move = board_inst[x, y]
                if isinstance(possible_next_move, Empty):
                    self.valid_moves.append((x, y))
                    [x, y] = [x + direction[0], y + direction[1]]
                elif possible_next_move.color != self.color:
                    self.valid_moves.append((x, y))
                    break
                else:
                    break

# endregion Rook


# region Knight
class Knight(Piece):
    name = "Knight"
    short_name = "N"
    strength = 3

    def update_valid_moves(self, board_inst):
        """
        This method updated the list of valid moves of the current chess piece

        :param board_inst: (Dict{8, 8}) The current state of the chess pieces on the board
        :return: None
        """
        self.clear_valid_moves()

        i = self.row
        j = self.col

        list_positions = []
        list_abstract_positions = [{
            'x': 1,
            'y': 2
        }, {
            'x': 2,
            'y': 1
        }]

        def append_to_list_positions(x1, y1):
            list_positions.append({
                'x': x1,
                'y': y1
            })

        for position in list_abstract_positions:
            (x, y) = (position['x'], position['y'])
            if i - x >= 0 and j - y >= 0:
                append_to_list_positions(i - x, j - y)
            if i - x >= 0 and j + y <= 7:
                append_to_list_positions(i - x, j + y)
            if i + x <= 7 and j - y >= 0:
                append_to_list_positions(i + x, j - y)
            if i + x <= 7 and j + y <= 7:
                append_to_list_positions(i + x, j + y)

        for position in list_positions:
            (x, y) = (position['x'], position['y'])
            possible_next_move = board_inst[x, y]
            if isinstance(possible_next_move, Empty) or \
                    self.color != possible_next_move.color:
                self.valid_moves.append((x, y))

# endregion Knight


# region Bishop
class Bishop(Piece):
    name = "Bishop"
    short_name = "B"
    strength = 3

    def update_valid_moves(self, board_inst):
        """
        This method updated the list of valid moves of the current chess piece

        :param board_inst: (Dict{8, 8}) The current state of the chess pieces on the board
        :return: None
        """
        self.clear_valid_moves()

        i = self.row
        j = self.col

        def list_directions():
            return [[-1, -1], [-1, 1], [1, -1], [1, 1]]

        for direction in list_directions():
            [x, y] = [i + direction[0], j + direction[1]]

            while True:
                if (x < 0 or x > 7) or \
                        (y < 0 or y > 7):
                    break

                possible_next_move = board_inst[x, y]
                if isinstance(possible_next_move, Empty):
                    self.valid_moves.append((x, y))
                    [x, y] = [x + direction[0], y + direction[1]]
                elif possible_next_move.color != self.color:
                    self.valid_moves.append((x, y))
                    break
                else:
                    break

# endregion Bishop


# region Queen
class Queen(Piece):
    name = "Queen"
    short_name = "Q"
    strength = 9

    def update_valid_moves(self, board_inst):
        """
        This method updated the list of valid moves of the current chess piece

        :param board_inst: (Dict{8, 8}) The current state of the chess pieces on the board
        :return: None
        """
        self.clear_valid_moves()

        i = self.row
        j = self.col

        def list_directions():
            return [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

        for direction in list_directions():
            [x, y] = [i + direction[0], j + direction[1]]

            while True:
                if (x < 0 or x > 7) or \
                        (y < 0 or y > 7):
                    break

                possible_next_move = board_inst[x, y]
                if isinstance(possible_next_move, Empty):
                    self.valid_moves.append((x, y))
                    [x, y] = [x + direction[0], y + direction[1]]
                elif possible_next_move.color != self.color:
                    self.valid_moves.append((x, y))
                    break
                else:
                    break
# endregion Queen


# region King
class King(Piece):
    name = "King"
    short_name = "K"
    strength = 90
    has_been_moved = False
    is_in_check = False

    def update_valid_moves(self, board_inst):
        """
        This method updated the list of valid moves of the current chess piece

        :param board_inst: (Dict{8, 8}) The current state of the chess pieces on the board
        :return: None
        """
        self.clear_valid_moves()

        i = self.row
        j = self.col

        list_directions = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

        for direction in list_directions:
            [x, y] = [i + direction[0], j + direction[1]]
            if (x < 0 or x > 7) or \
                    (y < 0 or y > 7):
                continue

            possible_next_move = board_inst[x, y]
            if isinstance(possible_next_move, Empty) or \
                    self.color != possible_next_move.color:

                if self.validate_next_position(board_inst, x, y) is True:
                    self.valid_moves.append((x, y))

        # small castling
        if self.has_been_moved is False and \
                self.col == 4 and \
                isinstance(board_inst[self.row, 7], Rook) and \
                board_inst[self.row, 7].has_been_moved is False and \
                isinstance(board_inst[self.row, 5], Empty) and \
                isinstance(board_inst[self.row, 6], Empty) and \
                self.validate_next_position(board_inst, self.row, 6) is True:
            self.valid_moves.append((self.row, 6))

        # long castling
        if self.has_been_moved is False and \
                self.col == 4 and \
                isinstance(board_inst[self.row, 0], Rook) and \
                board_inst[self.row, 0].has_been_moved is False and \
                isinstance(board_inst[self.row, 3], Empty) and \
                isinstance(board_inst[self.row, 2], Empty) and \
                isinstance(board_inst[self.row, 1], Empty) and \
                self.validate_next_position(board_inst, self.row, 2) is True:
            self.valid_moves.append((self.row, 2))

    def validate_next_position(self, board_inst, next_row, next_col):
        """
        This function checks if the next possible position of the \"King\" chess piece would be in
                     check if the \"King\" would be moves there.

        :param board_inst: The board instance on which the chess piece will be drawn
        :param next_row: The row position of the next move
        :param next_col: The column position of the next move
        :return: Boolean (True of False)
        """
        from board import Board
        board_handler = Board()
        board_handler.board_inst = copy.deepcopy(board_inst)

        board_handler.board_inst[self.row, self.col] = Empty(self.row, self.col, None)
        board_handler.board_inst[next_row, next_col] = Pawn(next_row, next_col, self.color)
        board_handler.update_valid_moves()

        for i in range(board_handler.rows):
            for j in range(board_handler.cols):
                if isinstance(board_handler.board_inst[i, j], Empty) or \
                        board_handler.board_inst[i, j].color == self.color or \
                        len(board_handler.board_inst[i, j].valid_moves) == 0:
                    continue

                for move in board_handler.board_inst[i, j].valid_moves:
                    if move[0] == next_row and move[1] == next_col:

                        # special case for the Pawns
                        if isinstance(board_handler.board_inst[i, j], Pawn) and \
                                next_col == j:
                            continue

                        return False
        return True

    def move(self, row, col):
        """
        This method updates the position of the current chess piece

        :param row: (Integer) The updated row value
        :param col: (Integer) The updated column value
        :return: None
        """
        super().move(row, col)
        self.has_been_moved = True

# endregion King


# region Pawn
class Pawn(Piece):
    name = "Pawn"
    strength = 1
    initial_position = True
    initial_move = False

    def update_valid_moves(self, board_inst):
        """
        This method updated the list of valid moves of the current chess piece

        :param board_inst: (Dict{8, 8}) The current state of the chess pieces on the board
        :return: None
        """
        self.clear_valid_moves()

        i = self.row
        j = self.col

        if self.color == 'black':
            k = 1
        elif self.color == 'white':
            k = -1
        else:
            return False

        if (self.color == 'black' and i < 7) or \
                (self.color == 'white' and i > 0):
            # FORWARD
            possible_next_move = board_inst[i + k, j]
            if isinstance(possible_next_move, Empty):
                self.valid_moves.append((i + k, j))

            # DIAGONAL
            if j < 7:
                possible_next_move = board_inst[i + k, j + 1]
                if (not isinstance(possible_next_move, Empty) and
                    self.color != possible_next_move.color) or \
                        (isinstance(possible_next_move, Empty) and  # en passant
                         isinstance(board_inst[i, j + 1], Pawn) and
                         board_inst[i, j + 1].color != self.color and
                         board_inst[i, j + 1].initial_move is True):
                    self.valid_moves.append((i + k, j + 1))

            if j > 0:
                possible_next_move = board_inst[i + k, j - 1]
                if (not isinstance(possible_next_move, Empty) and
                    self.color != possible_next_move.color) or \
                        (isinstance(possible_next_move, Empty) and  # en passant
                         isinstance(board_inst[i, j - 1], Pawn) and
                         board_inst[i, j - 1].color != self.color and
                         board_inst[i, j - 1].initial_move is True):
                    self.valid_moves.append((i + k, j - 1))

        if self.initial_position is True:
            if (self.color == 'black' and i == 1) or \
                    (self.color == 'white' and i == 6):
                possible_next_move = board_inst[i + 2 * k, j]
                if isinstance(possible_next_move, Empty):
                    self.valid_moves.append((i + 2 * k, j))

    def move(self, row, col):
        """
        This method updates the position of the current chess piece

        :param row: (Integer) The updated row value
        :param col: (Integer) The updated column value
        :return: None
        """
        super().move(row, col)
        self.initial_position = False

# endregion Pawn


# region Empty
class Empty(Piece):
    pass
# endregion Empty
