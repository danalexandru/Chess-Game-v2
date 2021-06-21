"""
This file contains the common functions and constants that will be used across the project
"""
import sys
from termcolor import colored

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

FLAG_DEBUG = True


# region GameMode
class GameMode(Enum):
    SINGLE_PLAYER = 0
    MULTI_PLAYER = 1
# endregion GameMode


GAME_MODE = GameMode.MULTI_PLAYER
# endregion constants


# region functions
def debug(message):
    """
    This method prints a message only if the FLAG_DEBUG flag is set to true

    :param message: (String) The message that we want to display
    :return: None
    """
    if FLAG_DEBUG:
        print(message)


def error(message):
    """
    This method prints an error message and exits the application

    :param message: (String) The message that we want to display
    :return:
    """
    print(colored(message, "red"), file=sys.stderr)
    sys.exit()

# endregion functions
