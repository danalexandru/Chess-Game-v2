"""
This file contains the common functions and constants that will be used across the project
"""
from enum import Enum

# region constants
GAME_WIDTH = 896
GAME_HEIGHT = 512
WIDTH = HEIGHT = 512
DIMENSION = 8
SQUARE_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15

TITLE = "Python Chess Game v0.1"
ICON = "Knight"


# region GameMode
class GameMode(Enum):
    SINGLE_PLAYER = 0
    MULTI_PLAYER = 1
# endregion GameMode


GAME_MODE = GameMode.MULTI_PLAYER
# endregion constants



