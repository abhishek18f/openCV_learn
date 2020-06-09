import numpy as np 
import cv2
# https://docs.opencv.org/master/d4/d13/tutorial_py_filtering.html

#LPF helps in removing noise, blurring images, etc.
# HPF filters help in finding edges in images.
img = cv2.imread('temp.jpg')

#AVERAGING/2D CONOLUTION
#it just convolves the image with uniform filter to take the average
#blur() , boxFilter() and filter2D can be used
kernel = (1/25)*np.ones((5,5) , dtype=np.float32)
img1 = cv2.filter2D(img, -1 , kernel)


#GAUSSIAN 
#it takes the weighted average of the neighbouring space pixels depending on the value of sigma

gaussian = cv2.GaussianBlur(img , (5,5) , 500)
cv2.imshow('img' , img)
cv2.imshow('average' , img1 )
cv2.imshow('gaussian' , gaussian )
cv2.waitKey(0)