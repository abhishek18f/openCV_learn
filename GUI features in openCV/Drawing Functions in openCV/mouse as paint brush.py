import cv2
import numpy as np 

#First we create a mouse callback function which is executed when a mouse event take place. 
# Mouse event can be anything related to mouse like left-button down, left-button up, left-button double-click etc. 
# It gives us the coordinates (x,y) for every mouse event. With this event and location, we can do whatever we like.

#Creating mouse callback function

def draw_circle(event , x, y, flags , params):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img , (x,y), 200 , (255,0,0) , 5)

# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3) , np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while(1):
    cv2.imshow('image' , img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()

