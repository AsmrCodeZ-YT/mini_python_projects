# owner2plusai
import cv2 as cv
import math

image_path = "s (7).jpg"
img = cv.imread(image_path)


point_list = []

def mouse_point(event,x,y,flag,params):
    
    if event == cv.EVENT_LBUTTONDOWN:
        
        #drow line from point 1 to point 2
        size = len(point_list)
        if size != 0 and size % 3 !=0:
            cv.line(img ,tuple(
                point_list[round((size-1)/3)*3]) ,(x,y), (0,255,0),3)

        # show click mouse 
        cv.circle(img,(x,y),5,(0,255,0),cv.FILLED)
        point_list.append([x,y])
        
        
def grad(pts1,pts2):
    return ((pts2[1]-pts1[1]) / (pts2[0]-pts1[0]))       
        

def get_angel(point_list):
    pts1,pts2,pts3 = point_list[-3:]
    
    m1 = grad(pts1,pts2)
    m2 = grad(pts1,pts3)
    
    # tan(a) = m2 - m1 /1 +(m2 *m1)
    angR = math.atan((m2 - m1)/(1 + (m2 * m1)))
    
    # round num
    ang_round = round(math.degrees(angR))
    
    # absolute value
    abs_val = abs(ang_round)
    
    
    # show text
    cv.putText(img, str(abs_val) ,
               (pts1[0], pts1[1]),cv.FONT_HERSHEY_COMPLEX ,1 ,(255,0,0),3)





while True:
    #check if we have 3 points
    if len(point_list) % 3==0 and len(point_list) !=0:
          get_angel(point_list)  
    
    
    cv.imshow("image" , img)
    cv.setMouseCallback("image",mouse_point)
    # break 
    
    #refresh
    if cv.waitKey(1) & 0xFF == ord("r"):
        point_list = []
        img = cv.imread(image_path)
    # break
    elif cv.waitKey(1) & 0xFF == ord("q"):
        break