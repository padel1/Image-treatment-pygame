import pygame

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.Info(
).current_w, pygame.display.Info().current_h


BG_COLOR = (22, 27, 37)

MAIN_IMAGE_SIZE = (300, 300)


class Drop_Down:
    choose_op = "choose op"
    conversion = "conversion"
    histogram = "histogram"
    rotate = "rotate"
    scale = "scale"
    conteur = "conteur"

    def __init__(self) -> None:

        pass
