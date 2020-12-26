"""
The main part of the project that starts and runs the program
"""
# region imports
import pygame
import os

import common
from board import Board


# endregion imports


# region load_images
def load_images():
    """
    This function loads the images of all the chess pieces and returns them in dictionary form
    :return: Dictionary containing all the images transformed to fit the chessboard squares
    {
        "black": {<pygame.image>, ...},
        "white": {<pygame.image>, ...}
    }
    """
    pieces = ["Rook", "Knight", "Bishop", "Queen", "King", "Pawn"]
    dict_images = {
        "black": {},
        "white": {}
    }
    for piece in pieces:
        dict_images["black"][piece] = pygame.transform.scale(pygame.image.load(os.path.join("pics",
                                                                                            "black",
                                                                                            piece + ".png")),
                                                             (common.SQUARE_SIZE, common.SQUARE_SIZE))
        dict_images["white"][piece] = pygame.transform.scale(pygame.image.load(os.path.join("pics",
                                                                                            "white",
                                                                                            piece + ".png")),
                                                             (common.SQUARE_SIZE, common.SQUARE_SIZE))

    return dict_images


# endregion load_images


# region redraw_game_state
def redraw_game_state(screen, board, dict_images):
    """
    This method draws the current state of the chessboard

    :param screen: (pygame.display) Pygame module to control the display window and screen
    :param board: (Dict{8, 8}) The current state of the chess pieces on the board
    :param dict_images: (Dict{"black": {}, "white": {}}) Dictionary containing the images of the chess pieces
    :return: Boolean (True or False)
    """
    if not redraw_empty_board(screen, board):
        return False

    if not redraw_highlighted_board_instances(screen, board):
        return False

    if not redraw_board_instance(screen, board, dict_images):
        return False

    pygame.display.update()
    return True


def redraw_empty_board(screen, board):
    """
    This method draws an empty chessboard

    :param screen: (pygame.display) Pygame module to control the display window and screen
    :param board: (Dict{8, 8}) The current state of the chess pieces on the board
    :return: Boolean (True or False)
    """
    colors = [pygame.Color(235, 235, 208), pygame.Color(119, 148, 85)]
    for row in range(board.rows):
        for col in range(board.cols):
            color = colors[(row + col) % 2]
            pygame.draw.rect(screen, color, pygame.Rect(col * common.SQUARE_SIZE, row * common.SQUARE_SIZE,
                                                        common.SQUARE_SIZE, common.SQUARE_SIZE))

    return True


def redraw_highlighted_board_instances(screen, board):
    """
    This function highlights the selected chess piece, as well as it's valid moves

    :param screen: (pygame.display) Pygame module to control the display window and screen
    :param board: (Dict{8, 8}) The current state of the chess pieces on the board
    :return: Boolean (True or False)
    """
    highlighted_color = pygame.Color(246, 246, 130)
    for row in range(board.rows):
        for col in range(board.cols):
            if board.get_piece((row, col)).is_selected:
                pygame.draw.rect(screen, highlighted_color,
                                 pygame.Rect(col * common.SQUARE_SIZE, row * common.SQUARE_SIZE,
                                             common.SQUARE_SIZE, common.SQUARE_SIZE))

    return True


def redraw_board_instance(screen, board, dict_images):
    """
    This method draws the remaining chess pieces on the empty board

    :param screen: (pygame.display) Pygame module to control the display window and screen
    :param board: (Dict{8, 8}) The current state of the chess pieces on the board
    :param dict_images: (Dict{"black": [], "white": []}) Dictionary containing the images of the chess pieces
    :return: Boolean (True or False)
    """
    from piece import Empty
    for row in range(board.rows):
        for col in range(board.cols):
            piece = board.get_piece((row, col))

            if not isinstance(piece, Empty):
                screen.blit(dict_images[piece.color][piece.name],
                            pygame.Rect(col * common.SQUARE_SIZE, row * common.SQUARE_SIZE,
                                        common.SQUARE_SIZE, common.SQUARE_SIZE))
    return True


# endregion redraw_game_state


# region click_on_chessboard
def click_on_chessboard(mouse_position):
    """
    This method determines on what square on the chessboard the user has clicked

    :param mouse_position: ((<COL_VALUE>, <ROW_VALUE>)) The current mouse position
    :return: (Integer, Integer) The selected square
    """
    if mouse_position[0] < 0 or mouse_position[0] > common.WIDTH:
        return False

    if mouse_position[1] < 0 or mouse_position[1] > common.HEIGHT:
        return False

    col = mouse_position[0] // common.SQUARE_SIZE
    row = mouse_position[1] // common.SQUARE_SIZE

    return row, col


# endregion click_on_chessboard


# region main
def main():
    """
    This method is called when the game is initialized. It will continue to run for the entirety of the duration of the
    game
    :return: None
    """
    print("... Starting chess game v0.1")
    pygame.init()
    screen = pygame.display.set_mode((common.GAME_WIDTH, common.GAME_HEIGHT))

    pygame.display.set_caption(common.TITLE)
    pygame.display.set_icon(pygame.image.load(os.path.join("pics",
                                                           "white",
                                                           "Knight.png")))
    clock = pygame.time.Clock()
    pygame.font.init()

    screen.fill(pygame.Color("white"))

    board = Board()
    dict_images = load_images()
    position = False

    run = True
    while run:
        clock.tick(common.MAX_FPS)
        if not redraw_game_state(screen, board, dict_images):
            run = False
            pygame.quit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_current_position = pygame.mouse.get_pos()
                last_position = position
                position = click_on_chessboard(mouse_current_position)

                if position is not False:
                    board.select(position)
                    common.debug("Position: (%d, %d)" % (position[0], position[1]))

                if position is not False and last_position is not False:
                    if board.is_move_valid(last_position, position):
                        board.move(last_position, position)
                        position = False
                        board.cancel()


if __name__ == "__main__":
    main()
# endregion main
