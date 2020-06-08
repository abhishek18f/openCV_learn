import numpy as np 
import cv2


img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainsvmimage.png')

#IMAGE ADDITION
#method 1 - directly add two images [OF SAME SIZE AND DEPTH]
new_img  = img1 + img2

#method2 - use cv2.add function
new_img1 = cv2.add(img1 , img2)

#There is a difference between OpenCV addition and Numpy addition.
#OpenCV addition is a saturated operation while Numpy addition is a modulo operation.

#Image Blending
#we can define weights to each image while adding
#final_img = alpha*img1 + beta*img2 + gamma

final_img = cv2.addWeighted(img1 , 0.4 , img2 , 0.7 , 0)

cv2.imshow('numpy addition' , new_img)
cv2.imshow('cv2.add' , new_img1)
cv2.imshow('blending' , final_img)
cv2.waitKey(0)


