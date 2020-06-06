import numpy as np 
import cv2

img = np.zeros((512,512,3) , np.uint8)          #for creating a black image

#Draw black line with thickness 5px of blue(BGR) color
img = cv2.line(img, (0,0) , (511,511) , (255,0,0), 5)

#drawing a rect.
cv2.rectangle(img, (288,0) , (444, 210) , (0,0,255) , 5)

#drawing a circle
cv2.circle(img , (222,222) , 50 , (255,255,255) , 5 , cv2.LINE_AA)

#drawing a polygon
cordinates = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)     #points into an array of shape ROWSx1x2
img = cv2.polylines(img , [cordinates] , False , (52,88,44), 5 , cv2.LINE_AA)


#cv2.polylines() can be used to draw multiple lines. 
# Just create a list of all the lines you want to draw and pass it to the function. All lines will be drawn individually.
#  It is more better and faster way to draw a group of lines than calling cv2.line() for each line.

#put Text
img = cv2.putText(img , 'Abhishek' , (10,485) , cv2.FONT_HERSHEY_COMPLEX , 3 , (255,255,255) , 5 , cv2.LINE_AA)

cv2.imshow('image' , img)
cv2.waitKey(0)
cv2.imwrite('draw.jpg' , img)
