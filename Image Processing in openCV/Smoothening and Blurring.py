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


#KERNEL SIZE SHOULD BE POSITIVE ODD INTEGER
#GAUSSIAN 
#it takes the weighted average of the neighbouring space pixels depending on the value of sigma
gaussian = cv2.GaussianBlur(img , (5,5) , 500)

#MEDIAN BLURRING
#it takes the median of the neighbouring space pixels and replaces the middle pixel with it
img2 = cv2.medianBlur(img, 5)

#BILATERAL FILTERING
#http://people.csail.mit.edu/sparis/bf_course/
#cv.bilateralFilter() is highly effective in noise removal while keeping edges sharp.
# Bilateral filtering also takes a Gaussian filter in space, but one more Gaussian filter which is a function of pixel difference.
# The Gaussian function of space makes sure that only nearby pixels are considered for blurring, 
# while the Gaussian function of intensity difference makes sure that only those pixels with similar intensities to the central pixel are considered for blurring. 
# So it preserves the edges since pixels at edges will have large intensity variation.
img3 = cv2.bilateralFilter(img, 5, 25, 1500)

cv2.imshow('img' , img)
cv2.imshow('average' , img1 )
cv2.imshow('gaussian' , gaussian )
cv2.imshow('median' , img2 )
cv2.imshow('bilateral' , img3)
cv2.waitKey(0)