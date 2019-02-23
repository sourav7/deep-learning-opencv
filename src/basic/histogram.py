#built-in Library import
import cv2
import numpy as np
from matplotlib import pyplot as plt
#custom module import
from src.basic import imageInfo

print(imageInfo.photographyImage)

image = cv2.imread(imageInfo.photographyImage)
histogram = cv2.calcHist([image],[0],None, [256],[0,256])

#we plot a histogram, ravel() flatens our image array
#i.e. two dimensional array into single dimension
plt.hist(image.ravel(), 256,[0,256])
plt.show()

#viewing separate color channels
color = ('b','g','r')

for i, col in enumerate(color):
    print(i)
    histogram2 = cv2.calcHist([image],[i],None,[256],[0,256])
    plt.plot(histogram2, color = col)
    plt.xlim([0,256])

plt.show()


# cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])

#     images : it is the source image of type uint8 or float32. it should be given in square brackets, ie, "[img]".
#     channels : it is also given in square brackets. It is the index of channel for which we calculate histogram. For example, if input is grayscale image, its value is [0]. For color image, you can pass [0], [1] or [2] to calculate histogram of blue, green or red channel respectively.
#     mask : mask image. To find histogram of full image, it is given as "None". But if you want to find histogram of particular region of image, you have to create a mask image for that and give it as mask. (I will show an example later.)
#     histSize : this represents our BIN count. Need to be given in square brackets. For full scale, we pass [256].
#     ranges : this is our RANGE. Normally, it is [0,256].

