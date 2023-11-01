import cv2
import numpy as np
import pygame

import cv2 as cv


class Operation:
    def __init__(self):
        pass

    @staticmethod
    def convert_hsv_to_rgb(image):
        return cv2.cvtColor(image, cv2.COLOR_HSV2RGB)
    @staticmethod
    def convert_binary_to_ng(image):
        height, width = image.shape

        gray_image = np.zeros((height, width), dtype=np.uint8)

        for i in range(height):
            for j in range(width):
                if image[i, j] == 0:
                    gray_image[i, j] = 0  # Set as black
                else:
                    gray_image[i, j] = 255  # Set as white

        return gray_image
    @staticmethod
    def convert_ycbcr_to_hsv(image):
        return cv2.cvtColor(image, cv2.COLOR_HSV2RGB)
    @staticmethod
    def convert_rgb_to_hsv(image):
        return cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    @staticmethod
    def convert_ycbcr_to_rgb(image):
        return cv2.cvtColor(image, cv2.COLOR_YCrCb2RGB)
    @staticmethod
    def convert_rgb_to_ycbcr(image):
        return cv2.cvtColor(image, cv2.COLOR_RGB2YCrCb)


    def convert(self, image, from_space, to_space):
        # cv_image = self.pygameSurfaceToCv2Image(image)
        if from_space == to_space:
            # No need to convert if source and target color spaces are the same
            return image
        else:
            conversion_function = getattr(
                self, f'convert_{from_space.lower()}_to_{to_space.lower()}')
            if callable(conversion_function):
                return conversion_function(image)
