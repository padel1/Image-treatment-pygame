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
        b, g, r = cv.split(image)

        r, g, b = r / 255.0, g / 255.0, b / 255.0

        h = np.zeros_like(r, dtype=np.float32)
        s = np.zeros_like(r, dtype=np.float32)
        v = np.zeros_like(r, dtype=np.float32)

        max_val = np.maximum(np.maximum(r, g), b)
        min_val = np.minimum(np.minimum(r, g), b)

        v = max_val

        s = np.where(max_val != 0, (max_val - min_val) / max_val, 0)

        for i in range(len(h)):
            for j in range(len(h[0])):
                if v[i][j] == r[i][j]:
                    h[i][j] = 60 * (g[i][j] - b[i][j]) / \
                        (v[i][j] - min(r[i][j], g[i][j], b[i][j]))
                elif v[i][j] == g[i][j]:
                    h[i][j] = 120 + 60 * (b[i][j] - r[i][j]) / \
                        (v[i][j] - min(r[i][j], g[i][j], b[i][j]))
                elif v[i][j] == b[i][j]:
                    h[i][j] = 240 + 60 * (r[i][j] - g[i][j]) / \
                        (v[i][j] - min(r[i][j], g[i][j], b[i][j]))
                elif r[i][j] == g[i][j] and r[i][j] == b[i][j]:
                    h[i][j] = 0

        h = (h + 360) % 360

        h = (np.round(h / 2)).astype(np.uint8)
        s = (s * 255).astype(np.uint8)
        v = (v * 255).astype(np.uint8)

        hsv_image = cv.merge([h, s, v])
        return hsv_image

    @staticmethod
    def convert_rgb_to_hsv_opencv(image):
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
