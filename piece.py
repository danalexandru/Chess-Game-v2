"""
The part of the project that deals with the logic of individual chess pieces
"""


# region Piece
class Piece(object):
    name = ""
    short_name = ""
    is_selected = False

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

# endregion Piece


# region Rook
class Rook(Piece):
    name = "Rook"
    short_name = "R"

# endregion Rook


# region Knight
class Knight(Piece):
    name = "Knight"
    short_name = "N"

# endregion Knight


# region Bishop
class Bishop(Piece):
    name = "Bishop"
    short_name = "B"

# endregion Bishop


# region Queen
class Queen(Piece):
    name = "Queen"
    short_name = "Q"

# endregion Queen


# region King
class King(Piece):
    name = "King"
    short_name = "K"

# endregion King


# region Pawn
class Pawn(Piece):
    name = "Pawn"


# endregion Pawn


# region Empty
class Empty(Piece):
    pass
# endregion Empty
