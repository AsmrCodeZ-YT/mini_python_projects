# owner2plusai YouTube : http://www.youtube.com/@owner2plusai

import cv2 as cv
from cv2 import aruco
import numpy as np

marker_dic = aruco.getPredefinedDictionary(aruco.DICT_6X6_250)
param_markers = aruco.DetectorParameters()
cap = cv.VideoCapture(0)



while True:
    success , img = cap.read()
    # break
    if not success:
        break
    
    gray_img = cv.cvtColor(img ,cv.COLOR_BGR2GRAY)
    marker_corners , marker_ID , reject = aruco.detectMarkers(
        gray_img, marker_dic,parameters=param_markers)

    if marker_corners:
        
        for ids,corners in zip(marker_ID,marker_corners):
            
            cv.polylines(img ,[corners.astype(np.int32)],True ,(0,255 ,255),
                         4, cv.LINE_AA)
            
            corners = corners.reshape(4,2)
            corners = corners.astype(int)
            top_right = corners[0].ravel()
            # num IDs
            cv.putText(img ,f"ID : {ids[0]}" ,top_right-5 ,
                       cv.FONT_HERSHEY_COMPLEX ,1,(0,255 ,255),2,cv.LINE_AA)
    
    
    cv.imshow("img", img)
    key = cv.waitKey(1)
    if key == ord("q"):
        break