import numpy as np 
import cv2


draw = False    #if True, then draw
x1 , y1 = -1 , -1
refPt = []

#Creating mouse callback function
def crop(event , x , y , flags , params ):
    global img , img2 , draw , x1 , y1 , refPt

    #drawing cropping rectangle
    if event == cv2.EVENT_LBUTTONDOWN:
        draw = True
        x1 , y1 = x , y
        refPt = [(x,y)]

    if event == cv2.EVENT_MOUSEMOVE:
        if draw == True:
            img = img2.copy()
            cv2.rectangle(img , (x1,y1) , (x,y) , (0,0,255) , 1)

    elif event == cv2.EVENT_LBUTTONUP:
        draw = False
        refPt.append((x,y))
        img = img2.copy()
        cv2.rectangle(img , (x1,y1) , (x,y) , (0,0,255) , 1)


#img = np.zeros((512,512,3) , np.uint8) 
img = cv2.imread('temp.jpg',0)
img2 = img.copy()  
cv2.namedWindow('image')
cv2.setMouseCallback('image' , crop)

#cropping selected image
while(1):
    # display the image and wait for a keypress
    cv2.imshow('image' ,img)
    key = cv2.waitKey(1) & 0xFF

    #reset
    if key == ord('r'):
        img = img2.copy()

    if key == ord('c'):
        if len(refPt) == 2:
            cropImg = img2[ refPt[0][1]:refPt[1][1] , refPt[0][0]:refPt[1][0] ]
            cv2.imshow('cropped_image' , cropImg)
            cv2.waitKey(0)
            break
    
    if key == ord('q'):
        break

cv2.destroyAllWindows()



