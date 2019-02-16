import cv2
import numpy as np


class Frame:
    'Frame class. Used to create backgrounds'

    def __init__(self, dimension, windowName):
        'Initialize image with dimension (with data type unsigned 8 bit int'
        self.image = np.zeros(dimension, np.uint8)
        self.windowName = windowName
    

    def showFrame(self):
        'Show frame with provided window name'
        cv2.imshow(self.windowName, self.image)
        cv2.waitKey()
        cv2.destroyWindow(self.windowName)
    
    def getFrame(self):
        return self.image
        


