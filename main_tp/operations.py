import cv2
import numpy as np
import pygame

import cv2 as cv


class Operation:
    def __init__(self):
        pass

    @staticmethod
    def convert_hsv_to_rgb(hsv_image):
        height, width, _ = hsv_image.shape


        rgb_image = np.zeros((height, width, 3), dtype=np.uint8)

        for i in range(height):
            for j in range(width):
                h, s, v = hsv_image[i, j]

                h /= 30.0
                s = s / 255.0
                v = v / 255.0


                c = v * s

                x = c * (1 - abs((h % 2) - 1))


                r, g, b = 0, 0, 0


                if 0 <= h < 1:
                    r, g, b = c, x, 0
                elif 1 <= h < 2:
                    r, g, b = x, c, 0
                elif 2 <= h < 3:
                    r, g, b = 0, c, x
                elif 3 <= h < 4:
                    r, g, b = 0, x, c
                elif 4 <= h < 5:
                    r, g, b = x, 0, c
                else:
                    r, g, b = c, 0, x

                m = v - c
                r, g, b = int((r + m) * 255), int((g + m) * 255), int((b + m) * 255)

                rgb_image[i, j] = [r, g, b]

        return rgb_image
    @staticmethod
    def convert_rgb_to_ng(image):
        print(image.shape)
            # Get the dimensions of the RGB image
        height, width, _ = image.shape

        # Create an empty grayscale image of the same size
        gray_image = np.zeros((height, width), dtype=np.uint8)

        # Convert each pixel to grayscale using the luminance method
        for y in range(height):
            for x in range(width):
                r, g, b = image[y, x]
                gray_value = int(0.2989 * r + 0.5870 * g + 0.1140 * b)
                gray_image[y, x] = gray_value

        return gray_image
    # @staticmethod
    # def convert_ng_to_rgb(gray_image):
    #     print(gray_image)
    #         # Get the dimensions of the grayscale image
    #     height, width,_ = gray_image.shape

    #     # Create an empty RGB image of the same size
    #     rgb_image = np.zeros((height, width,3), dtype=np.uint8)

    #     # Assign the grayscale value to all three color channels
    #     rgb_image[:, :, 0] = gray_image  # Red channel
    #     rgb_image[:, :, 1] = gray_image  # Green channel
    #     rgb_image[:, :, 2] = gray_image  # Blue channel

    #     return rgb_image
    @staticmethod
    def convert_rgb_to_hsv(image):
        b, g, r = cv.split(image)

        b, g, r = r / 255.0, g / 255.0, b / 255.0


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
                    h[i][j] = 60 * (g[i][j] - b[i][j]) / (v[i][j] - min(r[i][j], g[i][j], b[i][j]))
                elif v[i][j] == g[i][j]:
                    h[i][j] = 120 + 60 * (b[i][j] - r[i][j]) / (v[i][j] - min(r[i][j], g[i][j], b[i][j]))
                elif v[i][j] == b[i][j]:
                    h[i][j] = 240 + 60 * (r[i][j] - g[i][j]) / (v[i][j] - min(r[i][j], g[i][j], b[i][j]))
                elif r[i][j] == g[i][j] and r[i][j] == b[i][j]:
                    h[i][j] = 0
        

        h = (h + 360) % 360
       
        h = (np.round(h / 2)).astype(np.uint8)
        s = (s * 255).astype(np.uint8)
        v = (v * 255).astype(np.uint8)
      
        hsv_image = cv.merge([h, s, v])
        return hsv_image
    @staticmethod
    def convert_rgb_to_hsv1(image):
        return cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    @staticmethod
    def convert_ycbcr_to_rgb(image):
        conversion_matrix = np.array([
        [1.000, 1.403, 0.000],
        [1.000, -0.714, -0.344],
        [1.000, 0.000, 1.773]
        ])

        image_rgb = np.dot(image, conversion_matrix.T)
        

        image_rgb[..., 0] -= 128 * 1.403
        image_rgb[..., 1] += 128 * 1.058
        image_rgb[..., 2] -= 128 * 1.773
        
        # Clip and round the values to the [0, 255] range
        image_rgb = np.clip(image_rgb, 0, 255).round().astype('uint8')
        
        return image_rgb
    @staticmethod
    def convert_rgb_to_ycbcr(image):
        image_ycrcb = np.einsum('ij,nmj->nmi', [
        [0.299, 0.587, 0.114],
        [0.499813, -0.418531, -0.081282],
        [-0.168636, -0.331068, 0.499704]
        ], image)
        image_ycrcb[..., 1] += 128
        image_ycrcb[..., 2] += 128
        return np.round(image_ycrcb).astype('uint8')
    @staticmethod
    def convert_ycbcr_to_hsv(image):
        return Operation.convert_rgb_to_hsv(Operation.convert_ycbcr_to_rgb(image))
    

    def convert(self, image, from_space, to_space):
        # cv_image = self.pygameSurfaceToCv2Image(image)
        if from_space == to_space:
            # No need to convert if source and target color spaces are the same
            return image
        else:
            conversion_function_name = f'convert_{from_space.lower()}_to_{to_space.lower()}'
            conversion_function = getattr(self, conversion_function_name, None)
            if callable(conversion_function):
                return conversion_function(image)
            else :return cv2.imread("images/no_image.jpg")
