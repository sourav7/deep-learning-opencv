import cv2
import numpy as np

#custom module
from src.basic import imageInfo

#Coding Section
###############################
image = cv2.imread(imageInfo.photographyImage)


B, G, R = image[50,0]
print(image.shape)
print(B,G,R)

#convert to grayscale and see what happens
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

print(grayImage.shape)
print(grayImage[50,0])

#Convert to hsv image
hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.imshow('Hsv image', hsvImage)
cv2.imshow('Hue channel', hsvImage[:,:,0])
cv2.imshow('Saturation channel', hsvImage[:,:,1])
cv2.imshow('Value channel', hsvImage[:,:,2])

print('Hsv shape : ' ,hsvImage.shape)

cv2.waitKey()
cv2.destroyAllWindows()