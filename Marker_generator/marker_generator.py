import cv2 as cv
from cv2 import aruco


Input1 = input("MARKER SIZE :: ") 
Input2 = input("MARKER Num :: ") 

market_dict = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_6X6_250)

MARKER_SIZE = int(Input1)

for ID in range(int(Input2)):
    marker_image = aruco.generateImageMarker(market_dict,ID ,MARKER_SIZE )


    cv.imshow("img" , marker_image)
    cv.imwrite(f"marker_image/marker_image{ID}.png" ,marker_image)
    cv.waitKey(1)
