import cv2
import numpy as np

#custom module
from src.basic import imageInfo

#Coding Section
###############################
image = cv2.imread(imageInfo.photographyImage)


#split image into each color section
B, G, R = cv2.split(image)
print(B.shape)

#Lets create a matrix of zeros
# with dimensions of the image h x w
zeros = np.zeros(image.shape[:2], dtype="uint8")

cv2.imshow('Red', R)
cv2.imshow('Green', G)
cv2.imshow('Blue', B)

cv2.imshow('Merged', cv2.merge([B,G,R]))
cv2.imshow('Merged with blue amplified', cv2.merge([B+100,G,R]))
cv2.imshow('Merged with Red and Zero', cv2.merge([zeros,zeros,R]))

cv2.waitKey()
cv2.destroyAllWindows()