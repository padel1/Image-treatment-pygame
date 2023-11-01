import cv2

# Load an image in RGB format
image = cv2.imread('main_tp/images/rgb.png')

# Convert the image to HSV

hsv_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

# Save the converted image

cv2.imwrite('main_tp/images/hsv_image.png', hsv_image)
