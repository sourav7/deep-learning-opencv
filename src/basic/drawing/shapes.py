import cv2
import numpy as np
from src.basic.drawing.frame import Frame

#================Line================
#create a background to draw line
lineFrame = Frame((512,512,3),'Blue Line')
#create the line. The last argument is the thickness
cv2.line(lineFrame.getFrame(), (0,0),(511,511),(255,127, 0), 5)
#show the frame
lineFrame.showFrame()

#================Rectangle============
rectangleFrame = Frame((512,512,3),'Rectangle')
cv2.rectangle(rectangleFrame.getFrame(), (100,100),(300,250),(127,50,127),5)
rectangleFrame.showFrame()

#================Circle============
circleFrame = Frame((512,512,3),'Circle')
cv2.circle(circleFrame.getFrame(),(300,250),100,(127,50,127),-1)
circleFrame.showFrame()

#===========Polygons=========
polyFrame = Frame((512,512,3),'Polygon')
#define four points
pts = np.array([[10,50],[400,50],[90,200],[50,500]], np.int32)

#lets now reshape out points in form required by polylines
pts = pts.reshape((-1,1,2))

cv2.polylines(polyFrame.getFrame(), [pts], True, (0,0,255),3)
polyFrame.showFrame()