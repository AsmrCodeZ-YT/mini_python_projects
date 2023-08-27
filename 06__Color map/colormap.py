import cv2 as cv
import numpy as np


img = np.zeros((500,500,3),np.uint8)


def nothing():
    pass 

# Toolbar
cv.namedWindow("image")
cv.createTrackbar("R","image", 0,255 ,nothing)
cv.createTrackbar("G","image", 0,255 ,nothing)
cv.createTrackbar("B","image", 0,255 ,nothing)




while True:


    cv.imshow("image", img)

    r = cv.getTrackbarPos("R" ,"image")    
    g = cv.getTrackbarPos("G" ,"image")
    b = cv.getTrackbarPos("B" ,"image")

    
    img[:] = [b,g,r]

    # break
    if cv.waitKey(1) & 0xFF == ord("q"):
        break 

print(f"R:{r}",f"G:{g}",f"B:{b}")

cv.destroyAllWindows()