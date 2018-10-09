import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('messi5.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('image',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
