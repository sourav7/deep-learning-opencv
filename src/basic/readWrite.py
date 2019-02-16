import cv2
import numpy as np

#custom module
import imageInfo

# Load image using 'imread' specifying the path to image
image = cv2.imread(imageInfo.photographyImage)

# to display image variable
# first param is window name, 2nd is the image
cv2.imshow('Original Image', image)
# 'waitKey allows us to input information when a image window is open
# By leaving it blank it just waits for anykey to be pressed before
# continuining , By placing numbers (except 0)
#  we can specify a delay for how long you keep the window open(milliseconds)
cv2.waitKey()

grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Image', grayImage)
cv2.waitKey()

print(image.shape)
print('Height of image : ' , int(image.shape[0]) , ' pixels')
print('Width of image : ' , int(image.shape[1]) , ' pixels')

cv2.imwrite(imageInfo.outputImage, grayImage)

cv2.destroyAllWindows()
