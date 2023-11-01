import pygame
import cv2 as cv
from constant import *
from operations import Operation
import numpy as np


class Stage:
    def __init__(self) -> None:
        self.stage = "main"

    def kima_t7ab_l_blit(self, image):
        image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        return np.transpose(image, (1, 0, 2))

    def main(self, screen, image, x, y):
        image = self.kima_t7ab_l_blit(image)
        surf = pygame.surfarray.make_surface(image)
        screen.blit(surf, (x, y))

    def convertion(self, screen, image1, image2):
        image1 = self.kima_t7ab_l_blit(image1)
        image2 = self.kima_t7ab_l_blit(image2)
        img_rect = ((150, 190))
        screen.blit(pygame.transform.scale((pygame.surfarray.make_surface(image1)),MAIN_IMAGE_SIZE), img_rect)
        img_rect = ((SCREEN_WIDTH-(150+MAIN_IMAGE_SIZE[1]), 190))
        screen.blit(pygame.transform.scale((pygame.surfarray.make_surface(image2)),MAIN_IMAGE_SIZE), img_rect)
