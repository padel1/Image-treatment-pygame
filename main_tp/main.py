import sys
import pygame
from constant import *
from operations import Operation
from helper import Helper
from stages import Stage
import pygame_gui
import numpy as np
from tkinter import filedialog
from tkinter import Tk
import cv2 as cv
import copy


# new feature

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

helper = Helper()
root = helper.initialize_root()


# pygame gui items
manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT), "json.json")

options = [Drop_Down.choose_op, Drop_Down.conversion,
           Drop_Down.histogram, Drop_Down.rotate, Drop_Down.scale, Drop_Down.conteur]
dropdown = pygame_gui.elements.UIDropDownMenu(
    options_list=options,
    starting_option=options[0],
    relative_rect=pygame.Rect((SCREEN_WIDTH - 210, 10), (200, 70)),
    manager=manager,
)
load_image_btn = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((10, 10), (200, 40)), text="Load image", manager=manager
)
options_convert = ["choose", "BIN", "NG", "RGB", "HSV", "YCbCr"]
dropdown_convert_from = pygame_gui.elements.UIDropDownMenu(
    options_list=options_convert,
    starting_option="choose",
    relative_rect=pygame.Rect((400, 550), (100, 50)),
    manager=manager,
)
dropdown_convert_to = pygame_gui.elements.UIDropDownMenu(
    options_list=options_convert,
    starting_option="choose",
    relative_rect=pygame.Rect((790, 550), (100, 50)),
    manager=manager,
)
convert_btn = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((600, 600), (90, 40)), text="Convert", manager=manager
)
main_image = cv.imread("images/background.png")
resault_image = cv.imread("images/background.png")
widget = [dropdown_convert_from, dropdown_convert_to, convert_btn]


stage = Stage(Drop_Down.choose_op)

operation = Operation()
while True:
    screen.fill(BG_COLOR)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == load_image_btn:
                    path = helper.select_image()
                    main_image = cv.resize(cv.imread(path), (300, 300))
                    # main_image = pygame.transform.scale(
                    #     pygame.image.load(path), MAIN_IMAGE_SIZE
                    # )
                if event.ui_element == convert_btn:

                    resault_image = operation.convert(
                        main_image, dropdown_convert_from.selected_option, dropdown_convert_to.selected_option)

            elif event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:

                if event.ui_element == dropdown:

                    if dropdown.selected_option == Drop_Down.choose_op:

                        stage.stage = Drop_Down.choose_op

                    if dropdown.selected_option == Drop_Down.conversion:
                        stage.stage = Drop_Down.conversion

                    if dropdown.selected_option == Drop_Down.histogram:
                        stage.stage = Drop_Down.histogram
            

        manager.process_events(event)

    # manager setup
    manager.update(pygame.time.Clock().tick(60) / 1000.0)
    manager.draw_ui(screen)

    if stage.stage == Drop_Down.choose_op:

        stage.main(
            screen, main_image, SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 150
        )
        helper.widget_visibility(widget, [])
    elif stage.stage == Drop_Down.conversion:

        stage.convertion(screen, main_image, resault_image)
        helper.widget_visibility(
            widget, [dropdown_convert_from, dropdown_convert_to, convert_btn])
    elif stage.stage == Drop_Down.histogram:
        helper.widget_visibility(widget, [])
    pygame.display.update()
    # test
