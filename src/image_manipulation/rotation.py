import cv2
import numpy as np
from src.basic import imageInfo

image = cv2.imread(imageInfo.photographyImage)
height, width = image.shape[:2]

#divide by rwo to rate the image around its center
rotationMatrix = cv2.getRotationMatrix2D((width/2, height/2),45, 0.5)
print(rotationMatrix)

rotatedImage = cv2.warpAffine(image, rotationMatrix,(width, height))

rotatedByTranspose = cv2.transpose(image)

cv2.imshow("Rotated image", rotatedImage)
cv2.imshow("Rotated image by transpose",rotatedByTranspose)
cv2.waitKey()
cv2.destroyAllWindows()