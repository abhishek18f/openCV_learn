import numpy as np 
import cv2

img = np.zeros((512,512,3) , np.uint8)          #for creating a black image

#Draw black line with thickness 5px of blue(BGR) color
img = cv2.line(img, (0,0) , (511,511) , (255,0,0), 5)

#drawing a rect.



cv2.imshow('image' , img)
cv2.waitKey(0)
