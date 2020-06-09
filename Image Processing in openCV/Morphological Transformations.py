import numpy as np 
import cv2

# https://docs.opencv.org/trunk/d9/d61/tutorial_py_morphological_ops.html
# 

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    _ , frame = cap.read()
    
    #convert frame to hsv image
    #hsv = hue(mainly stores color details) , saturation(stores opacity) , value(stores something.. idk)
    hsv = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)

    #define range of color
    lower = np.array([150 , 150 , 150])             #this is for RED color
    upper = np.array([180, 255 , 255])

    #create mask
    mask = cv2.inRange(hsv ,lower ,upper)

    #Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame , frame , mask = mask)
    
    #APPLYING MORPHOLOGICAL TRANSFORMATIONS
    #EROSION
    kernel = np.ones((5,5) , np.uint8)
    #erosion basically erodes the noise and boundary points or outliners
    #kernal is traversed over image and it converts middle point to 1 if all points inside the kernel is 1(or of same color) otherwise zero
    erosion = cv2.erode(mask , kernel)

    #DILATION
    #it basically amplifies outliners/noises
    #kernal is traversed over image and it converts middle point to 1 if atleast one point inside the kernel is 1(or of same color) otherwise zero
    dilation = cv2.dilate(mask , kernel)

    #OPENING

    res_erode = cv2.bitwise_and(frame , frame , mask = dilation)
    cv2.imshow('frame' , frame)
    cv2.imshow('mask' , mask)
    cv2.imshow('erosion' , erosion)
    cv2.imshow('dilation' , dilation)
    cv2.imshow('res_erode' , res_erode)
    cv2.imshow('masked image', res)
    k = cv2.waitKey(5) & 0xFF
    if k == ord('q'): 
        break

cv2.destroyAllWindows()
cap.release()