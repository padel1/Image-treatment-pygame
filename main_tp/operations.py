import cv2
import numpy as np
import pygame

class Operation:
    def __init__(self):
        pass
    
    @staticmethod
    def convert_hsv_to_rgb(image):
        return cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
    @staticmethod
    def convert_rgb_to_hsv(image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    @staticmethod
    def convert_ycbcr_to_rgb(image):
        return cv2.cvtColor(image, cv2.COLOR_YCrCb2BGR)
    @staticmethod
    def convert_rgb_to_ycbcr(image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
    @staticmethod
    def pygameSurfaceToCv2Image(selected_area):
        image_object = np.array(pygame.surfarray.pixels3d(selected_area))
        # image_object = np.transpose(img_array, (1, 0, 2))
        image_object[:, :, [0, 2]] = image_object[:, :, [2, 0]]
        return image_object

    def convert(self,image, from_space, to_space):
        cv_image=self.pygameSurfaceToCv2Image(image)
        if from_space == to_space:
            # No need to convert if source and target color spaces are the same
            return image
        else:
            conversion_function = getattr(self, f'convert_{from_space.lower()}_to_{to_space.lower()}')
            if callable(conversion_function):
                return pygame.surfarray.make_surface(conversion_function(cv_image))
            
