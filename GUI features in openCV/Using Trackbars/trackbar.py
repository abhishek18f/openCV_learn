import numpy as np 
import cv2

#callback function - called everytime trackbar is move(value is changed)
def nothing(x):         #x is value of trackbar
    print(x)

img = np.zeros((512,512,3))

cv2.namedWindow('image')

#add 4 trackbar to the image window
cv2.createTrackbar('R' , 'image' , 0 , 255 , nothing)
cv2.createTrackbar('G' , 'image' , 0 , 255 , nothing)
cv2.createTrackbar('B' , 'image' , 0 , 255 , nothing)

greyscale = '0:color \n 1:greyscale'        #switch for changing into greyscale or can be used as on/off
cv2.createTrackbar(greyscale , 'image' , 0 , 1 , nothing)

while(1):
    cv2.imshow('image' , img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    r = cv2.getTrackbarPos('R' , 'image')
    g = cv2.getTrackbarPos('G' , 'image')
    b = cv2.getTrackbarPos('B' , 'image')
    switch = cv2.getTrackbarPos(greyscale , 'image')

    if switch == 1:
        img = cv2.cvtColor(img , cv2.COLOR_GRAY2BGR)
    elif switch == 0:
        img = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

    img[:]  = [b , g , r]    

    

cv2.destroyAllWindows()
