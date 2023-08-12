# @OWNER2PLUSAI 

import os 
import cv2 as cv
import numpy as np
import mediapipe as mp

# find images
image_path  = "images"
images = os.listdir(image_path)
image_index = 0
bg_image = cv.imread(image_path +"/" +images[image_index])

# pretrained model for human detection
mp_selfie_segmentation = mp.solutions.selfie_segmentation
selfie_segmentation = mp_selfie_segmentation.SelfieSegmentation(model_selection=1) # use segmentation 

cap = cv.VideoCapture("Video.mp4") # for ur webcam use 0 , 1 
while cap.isOpened():
    _ ,frame = cap.read()
    frame = cv.flip(frame,1)
    height ,width ,channle = frame.shape
    RGB = cv.cvtColor(frame ,cv.COLOR_BGR2RGB)
    results = selfie_segmentation.process(RGB)
    mask = results.segmentation_mask
    
    condition = np.stack(
        (results.segmentation_mask,) *3 ,axis=-1) > 0.5
    
    bg_image = cv.resize(bg_image, (width,height))
    output_image = np.where(condition,frame ,bg_image)
    
    cv.imshow("Webcam",output_image)
    cv.imshow("real",frame)
    
    key = cv.waitKey(15) # slow framerate
    if key == ord("q"): # press q for exit 
        break
    elif key == ord("d"): # press d for change background
        if image_index != len(images)-1:
            image_index += 1
        else:
            image_index = 0
        
        bg_image = cv.imread(image_path +"/" +images[image_index])



