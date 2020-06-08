import numpy as np 
import cv2

#PUTTING PYTHON LOGO IN TOP LEFT CORNER OF kenny image
img1 = cv2.imread('pythonlogo.png')
img2 = cv2.imread('temp.jpg')

#creating an ROI
rows , cols , depth = img1.shape
roi = img2[0:rows , 0:cols , 0:depth]

#cv2.imshow('dsd' , roi)
#cv2.waitKey(0)

#now for putting the logo we can simply replace ROI with logo
#But it will also put the white background
#To remove background , we use masking

#MASKING
#make grayscale for better masking
img2gray = cv2.cvtColor(img1 ,cv2.COLOR_BGR2GRAY)

#add a threshold -- basically convert image into 2 colors only based on threshold value
#ret stores threshold value and mask stores masked image
#https://docs.opencv.org/3.4/d7/d4d/tutorial_py_thresholding.html
ret  , mask = cv2.threshold(img2gray , 220 , 255 , cv2.THRESH_BINARY_INV)
#cv2.imwrite('inverse_masked_logo.png', mask)
mask_inv = cv2.bitwise_not(mask)
#cv2.imwrite('masked_logo.png' , mask_inv)


#Blackout the area of logo in ROI
img2_bg = cv2.bitwise_and(roi , roi , mask = mask_inv)
#cv2.imwrite('background.png' , img2_bg)

#take only logo part from logo
img1_fg = cv2.bitwise_and(img1 , img1 , mask=mask)
#cv2.imwrite('foreground.png' , img1_fg)

dest = cv2.add(img2_bg ,img1_fg)
#cv2.imwrite('final_logo.png' , dest)

img2[0:rows , 0:cols , 0:depth]  = dest
#cv2.imwrite('final.jpg' , img2)
#cv2.waitKey(0)
