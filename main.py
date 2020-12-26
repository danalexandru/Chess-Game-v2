"""
The main part of the project that starts and runs the program
"""
# region imports
import pygame
import os

import common


# endregion imports


# region load_images
def load_images():
    """
    This function loads the images of all the chess pieces and returns them in dictionary form
    :return: Dictionary containing all the images transformed to fit the chessboard squares
    {
        "black": [<pygame.image>, ...],
        "white": [<pygame.image>, ...]
    }
    """
    pieces = ["Rook", "Knight", "Bishop", "Queen", "King", "Pawn"]
    dict_images = {
        "black": [],
        "white": []
    }
    for piece in pieces:
        dict_images["black"].append(pygame.transform.scale(pygame.image.load(os.path.join("pics",
                                                                                          "black",
                                                                                          piece + ".png")),
                                                           (common.SQUARE_SIZE, common.SQUARE_SIZE)))
        dict_images["black"].append(pygame.transform.scale(pygame.image.load(os.path.join("pics",
                                                                                          "white",
                                                                                          piece + ".png")),
                                                           (common.SQUARE_SIZE, common.SQUARE_SIZE)))

    return dict_images


# endregion load_images


# region redraw_game_state
def redraw_game_state(screen):
    """
    This method draws the current state of the chessboard

    :param screen: (pygame.display) Pygame module to control the display window and screen
    :return: Boolean (True or False)
    """
    # Draw the empty board
    # colors = [pygame.Color("white"), pygame.Color("gray")]
    colors = [pygame.Color(235, 235, 208), pygame.Color(119, 148, 85)]
    for row in range(common.DIMENSION):
        for col in range(common.DIMENSION):
            color = colors[(row + col) % 2]
            pygame.draw.rect(screen, color, pygame.Rect(col * common.SQUARE_SIZE, row * common.SQUARE_SIZE,
                                                        common.SQUARE_SIZE, common.SQUARE_SIZE))

    pygame.display.update()
    return True


# endregion redraw_game_state


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

    run = True
    while run:
        clock.tick(common.MAX_FPS)
        if not redraw_game_state(screen):
            run = False
            pygame.quit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass


if __name__ == "__main__":
    main()
# endregion main
