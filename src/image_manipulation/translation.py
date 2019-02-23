import cv2
import numpy as np
from src.basic import imageInfo

image = cv2.imread(imageInfo.photographyImage)

# #store height and width of the image
height, width = image.shape[:2]

quarterHeight, quarterWidth = height/4, width/8

#         [1 0 Tx]
# T =     [0 1 Ty]

#T is our translation mmtrix
T = np.float_([[1,0,quarterWidth],[0,1,quarterHeight]])
# T = np.float_([[1,-1,quarterWidth],[0,1,quarterHeight]])


imgTranslation = cv2.warpAffine(image,T,(width,height))
cv2.imshow("Main image", image)
cv2.imshow("Translation", imgTranslation)
cv2.waitKey()
cv2.destroyAllWindows()

print(T)