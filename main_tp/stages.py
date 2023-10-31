import pygame
from constant import *
from operations import Operation

class Stage:
    def __init__(self) -> None:
        self.stage = "main"

    def main(slef,screen,image,x,y):
        screen.blit(image,(x,y))

    def convertion(self,screen,image1,image2):
        img_rect = ((150,190))
        screen.blit(image1, img_rect)
        img_rect = ((SCREEN_WIDTH-(150+MAIN_IMAGE_SIZE[1]),190))
        screen.blit(image2, img_rect)
        
