import cv2 as cv


inpt_image = input("Drage Ur image :: ")
img = cv.imread(inpt_image)

#1080 ,1920
w ,h ,d = img.shape

print(w,h)

# img = cv.imshow("image1",img_read)
img_resize = cv.resize(img, (int(h/2), int(w/2)))

def nothing():
    pass

cv.namedWindow("ToolBar")
cv.createTrackbar("R", "ToolBar" ,1 ,200, nothing)
cv.createTrackbar("G", "ToolBar" ,1 ,200, nothing)



while True:
    r = cv.getTrackbarPos("R","ToolBar")
    g = cv.getTrackbarPos("R","ToolBar")
    print(r,g,"For Finish Press 'q'")
    
    carton_style = cv.stylization(img_resize , sigma_r=(r/100) , sigma_s=(g/100) )
    # show image 
    cv.imshow("image1",carton_style )
    # press q to exit and write image
    if cv.waitKey(1) & 0xFF == ord("q"):
        break

# write on real img    
carton_style1 = cv.stylization(img , sigma_r=(r/100) , sigma_s=(g/100) )
cv.imwrite(f"output{r,g}.jpg",carton_style1)
cv.destroyAllWindows()