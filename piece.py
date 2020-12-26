"""
The part of the project that deals with the logic of individual chess pieces
"""


# region Piece
class Piece(object):
    name = ""
    short_name = ""

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color


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
