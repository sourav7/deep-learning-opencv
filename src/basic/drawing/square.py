import cv2
import numpy as np
from frame import Frame

#create a black image
image = np.zeros((512,512,3), np.uint8)
imageBw = np.zeros((512,512), np.uint8)


cv2.imshow('Black Rectangle (color image)', image)
cv2.imshow('Black Rectangle (B&W image)', imageBw)

cv2.waitKey()
cv2.destroyAllWindows()