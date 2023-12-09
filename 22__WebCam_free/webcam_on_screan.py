import cv2 as cv

#use 0 ,1 ,2  etc. 
cap = cv.VideoCapture(1) # for me zero 

while True:
    
    sucess , img = cap.read()
    print(img.shape)
    # resize frame 
    frame = cv.resize(img,(400 ,600))
    frame = img[100:]
    cv.imshow("WebCam", frame)
    # cant remove on screen
    cv.setWindowProperty("WebCam", cv.WND_PROP_TOPMOST ,1)
    if cv.waitKey(1) & 0xff == ord("q"): break    
    
cap.release()
cv.destroyAllWindows()