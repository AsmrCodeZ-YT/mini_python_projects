# owner2plusai

import cv2 as cv
import numpy as np

circles = np.zeros((4,2) ,np.int32)
counter_ = 0
# read mouse click
def mousePoint(event ,x ,y , flags ,params):
    global counter_
    if event == cv.EVENT_LBUTTONDOWN:
        circles[counter_] = x,y
        counter_ += 1
        
# read image file
img = cv.imread('src/1.jpg')
while True:
    if counter_ == 4:
        width , hight = 500, 600
        pts1 = np.float32([circles[0] , circles[1] , circles[2] ,circles[3]]) # side of the image
        pts2 = np.float32([[0,0] ,[width,0] ,[0,hight] ,[width,hight]]) # need list 
        # getPerspectiveTransform of image
        metrix = cv.getPerspectiveTransform(pts1, pts2)
        imgoutput = cv.warpPerspective(img , metrix ,(width , hight))
        cv.imshow("result" , imgoutput)
        
    for x in range(0,4):
        cv.circle(img ,(circles[x][0] , circles[x][1]) , 5 , (0,200 ,255) , cv.FILLED)

    cv.imshow('image', img)
    cv.setMouseCallback("image" ,mousePoint )
    if cv.waitKey(1) & 0xFF == ord('q'):
        break 
    
cv.destroyAllWindows()